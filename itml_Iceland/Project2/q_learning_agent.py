from flappy_agent import FlappyAgent
import random
import numpy as np

class QLearningAgent(FlappyAgent):
    def __init__(self):
        self.groundLevel = 0.79*512
        self.birdHeight = 24
        self.pipeDist = 283
        self.name = "QAgent"
        
        self.discount = 1.0
        self.learn_rate = 0.1
        self.epsilon = 0.1

        self.Q_table = np.zeros((15,15,15,19,2))

    
    def reward_values(self):
        """ returns the reward values used for training
        
            Note: These are only the rewards used for training.
            The rewards used for evaluating the agent will always be
            1 for passing through each pipe and 0 for all other state
            transitions.
        """
        return {"positive": 1.0, "tick": 0.0, "loss": -5.0}
    
    def observe(self, s1, a, r, s2, end):
        """ this function is called during training on each step of the game where
            the state transition is going from state s1 with action a to state s2 and
            yields the reward r. If s2 is a terminal state, end==True, otherwise end==False.
            
            Unless a terminal state was reached, two subsequent calls to observe will be for
            subsequent steps in the same episode. That is, s1 in the second call will be s2
            from the first call.
            """

        state = self.reduce_states(s1)
        i = int(state['player_y'])
        j = int(state['next_pipe_top_y'])
        k = int(state['next_pipe_dist_to_player'])
        l = int(state['player_vel'])

        state2 = self.reduce_states(s2)
        i2 = int(state2['player_y'])
        j2 = int(state2['next_pipe_top_y'])
        k2 = int(state2['next_pipe_dist_to_player'])
        l2 = int(state2['player_vel'])
        
        Q_s = self.Q_table[i][j][k][l]
        Q_s2 = self.Q_table[i2][j2][k2][l2]
        
        Q_s[a] = Q_s[a] + self.learn_rate * (r + self.discount * Q_s2.max() - Q_s[a])


    def training_policy(self, state):
        """ Returns the index of the action that should be done in state while training the agent.
            Possible actions in Flappy Bird are 0 (flap the wing) or 1 (do nothing).

            training_policy is called once per frame in the game while training
        """
        
        # With probability self.epsion, pick a random action
        if random.random() < self.epsilon:
            #Pick random action
            if random.random() < 0.5:
                return 0
            else:
                return 1
        
        #Else use greedy policy
        return self.policy(state)          


    def policy(self, state):
        """ Returns the index of the action that should be done in state when training is completed.
            Possible actions in Flappy Bird are 0 (flap the wing) or 1 (do nothing).

            policy is called once per frame in the game (30 times per second in real-time)
            and needs to be sufficiently fast to not slow down the game.
        """
        
        state = self.reduce_states(state)
        i = int(state['player_y'])
        j = int(state['next_pipe_top_y'])
        k = int(state['next_pipe_dist_to_player'])
        l = int(state['player_vel'])

        Q_s = self.Q_table[i][j][k][l]

        if Q_s[0] > Q_s[1]:
            return 0
        else:
            return 1    
    
    def reduce_states(self, state):
        new_state = {}
        velocity = state['player_vel']+8
        new_state['player_vel'] = velocity
        
        y_values = ['player_y', 'next_pipe_top_y']
        
        for field in y_values:
            if state[field] <= 0.0:
                new_state[field] = 0
            elif state[field] > self.groundLevel - self.birdHeight:
                new_state[field] = 14
            else:
                new_state[field] = state[field] * 14 // (self.groundLevel - self.birdHeight)
            
        field = 'next_pipe_dist_to_player'
        
        if state[field] <= 0.0:
            new_state[field] = 0
        elif state[field] > self.pipeDist:
            new_state[field] = 14
        else:
            new_state[field] = state[field] * 14 // self.pipeDist
        
        return new_state

    def get_policy_table(self):
        policy_table = np.zeros((15,15,15,19))
        for i in range(0, 15): # player_y
            for j in range(0, 15): # next_pipe_top_y
                for k in range(0, 15): # next_pipe_dist_to_player
                    for l in range(0, 19): # player_vel
                        Q_s = self.Q_table[i][j][k][l]
                        policy_table[i][j][k][l] = Q_s[1] - Q_s[0]
        return policy_table
