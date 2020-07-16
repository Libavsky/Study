from flappy_agent import FlappyAgent
import random
import numpy as np

class MonteCarloAgentBest(FlappyAgent):
    def __init__(self):
        self.name = ""
        self.groundLevel = 0.79*512
        self.birdHeight = 24
        self.pipeDist = 283
        self.epsilon = 0.05
        self.Q_table = np.zeros((15,15,15,19,2))
        self.policy_table = np.zeros((15,15,15,19))
        self.episode_table = np.zeros((15,15,15,19,2))
        self.episode_table_rewards = np.zeros((15, 15, 15, 19, 2))
        self.episode_list = []
        self.learning_rate = 0.1
        self.discount = 0.85
        self.reward_factor = 0.07
        self.episode_counter = 0

        for i in range (0,15):
            for j in range(0, 15):
                for k in range(0, 15):
                    for l in range(0, 19):
                        for m in range(0, 2):
                            self.Q_table[i][j][k][l][m]=0.0
                        self.policy_table[i][j][k][l]=0.5
    
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
        self.episode_list.append((i,j,k,l,a,r))
        if end:
            self.episode_counter+=1
            if self.episode_counter%100 == 0:
                self.epsilon*=0.95
            score=0
            z = len(self.episode_list)-1
            while z >= 0:
                distance = self.episode_list[z][1] - self.episode_list[z][0] + 1
                if self.episode_list[z][2]<11:
                    if distance<0:
                        if self.episode_list[z][3]>6:
                            velocity_factor = -1 * abs(distance)*2* self.reward_factor + (2* self.reward_factor)
                        else:
                            velocity_factor = -1 * abs(distance) / 2 * self.reward_factor + (self.reward_factor/2)
                    elif distance>0:
                        if self.episode_list[z][3]<11:
                            velocity_factor = -1 * abs(distance)*2* self.reward_factor + (2* self.reward_factor)
                        else:
                            velocity_factor = -1 * abs(distance) / 2 * self.reward_factor + (self.reward_factor/2)
                    else:
                        if self.episode_list[z][3]>6 or self.episode_list[z][3]<11:
                            velocity_factor = 0
                        else:
                            velocity_factor = self.reward_factor*2
                else:
                    if distance<0:
                        if self.episode_list[z][3]>6:
                            velocity_factor = (-1 * abs(distance)*2* self.reward_factor + (2* self.reward_factor))*1/(self.episode_list[z][2]-10)
                        else:
                            velocity_factor = (-1 * abs(distance) / 2 * self.reward_factor + (self.reward_factor/2))*1/(self.episode_list[z][2]-10)
                    elif distance>0:
                        if self.episode_list[z][3]<11:
                            velocity_factor = (-1 * abs(distance)*2* self.reward_factor + (2* self.reward_factor))*1/(self.episode_list[z][2]-10)
                        else:
                            velocity_factor = (-1 * abs(distance) / 2 * self.reward_factor + (self.reward_factor/2))*1/(self.episode_list[z][2]-10)
                    else:
                        if self.episode_list[z][3]>6 or self.episode_list[z][3]<11:
                            velocity_factor = 0
                        else:
                            velocity_factor = (self.reward_factor*2)*1/(self.episode_list[z][2]-10)
                score = score * self.discount + self.episode_list[z][5] + velocity_factor
                self.episode_table_rewards[self.episode_list[z][0]][self.episode_list[z][1]][self.episode_list[z][2]][self.episode_list[z][3]][self.episode_list[z][4]] = score
                self.episode_table[self.episode_list[z][0]][self.episode_list[z][1]][self.episode_list[z][2]][self.episode_list[z][3]][self.episode_list[z][4]]+=1
                z -= 1
            for i in range(0, 15): # player_y
                for j in range(0, 15): # next_pipe_top_y
                    for k in range(0, 15): # next_pipe_dist_to_player
                        for l in range(0, 19): # player_vel
                            for m in range(0, 2): # action
                                if self.episode_table[i][j][k][l][m]!=0:
                                    self.Q_table[i][j][k][l][m]= (1-self.learning_rate)*self.Q_table[i][j][k][l][m] + self.learning_rate*self.episode_table_rewards[i][j][k][l][m]
                                    if self.Q_table[i][j][k][l][1]>=self.Q_table[i][j][k][l][0]:
                                        self.policy_table[i][j][k][l]=(1-self.epsilon)+(self.epsilon/2)
                                    else:
                                        self.policy_table[i][j][k][l] = self.epsilon / 2

            # TODO: learn from the observation
            self.episode_table = np.zeros((15, 15, 15, 19, 2))
            self.episode_table_rewards = np.zeros((15, 15, 15, 19, 2))
            self.episode_list = []
        return

    def training_policy(self, state):
        """ Returns the index of the action that should be done in state while training the agent.
            Possible actions in Flappy Bird are 0 (flap the wing) or 1 (do nothing).

            training_policy is called once per frame in the game while training
        """
        #print("state: %s" % state)
        # TODO: change this to to policy the agent is supposed to use while training
        # At the moment we just return an action uniformly at random.
        #print("reduced state: %s" % self.reduce_states(state))
        state = self.reduce_states(state)
        i = int(state['player_y'])
        j = int(state['next_pipe_top_y'])
        k = int(state['next_pipe_dist_to_player'])
        l = int(state['player_vel'])

        temp=self.policy_table[i][j][k][l]
        temp*=100
        temp=int(temp)
        randi=random.randint(0, 100)
        if temp<randi:
            return 0
        else:
            return 1

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
        if self.policy_table[i][j][k][l]<0.5:
            return 0
        else:
            return 1
        # TODO: change this to to policy the agent has learned
        # At the moment we just return an action uniformly at random.
        #return random.randint(0, 1)
    
    def reduce_states(self, state):
        new_state = {}
        velocity = state['player_vel']+8
        new_state['player_vel'] = velocity
        
        y_values = ['player_y', 'next_pipe_top_y']
        
        #0 above screen, 1-13 top to bottom, 14 under bottom
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
        policy = np.copy(self.policy_table)
        sub = np.zeros((15,15,15,19))
        sub.fill(0.5)
        return policy - sub
