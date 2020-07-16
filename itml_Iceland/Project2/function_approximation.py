from q_learning_agent import QLearningAgent
import random
import numpy as np

class FunctionAgent(QLearningAgent):
    def __init__(self):
        QLearningAgent.__init__(self)
        self.name = "FunctionAgent"
        
        self.discount = 1.0
        self.learn_rate = 0.1
        self.epsilon = 0
        
        self.theta_flap = np.zeros(4)
        self.theta_noflap = np.zeros(4)
        self.Q_table = np.zeros((15,15,15,19,2))
    
    def observe(self, s1, a, r, s2, end):
        state = self.reduce_states(s1)
        i = int(state['player_y'])
        j = int(state['next_pipe_top_y'])
        k = int(state['next_pipe_dist_to_player'])
        l = int(state['player_vel'])
        Q_s = self.Q_table[i][j][k][l]

        if end:
            Q_s2 = np.zeros(2)
        else:
            state2 = self.reduce_states(s2)
            i2 = int(state2['player_y'])
            j2 = int(state2['next_pipe_top_y'])
            k2 = int(state2['next_pipe_dist_to_player'])
            l2 = int(state2['player_vel'])
            Q_s2 = self.Q_table[i2][j2][k2][l2]
    
        phi = [x for (_, x) in state.items()] # get a list from a dictionary
        target = r + self.discount * Q_s2.max()
        print("phi:", phi)
        print("target:", target)

        if a == 0:
            Q_s[a] = self.theta_flap.dot(phi)
            self.theta_flap = self.theta_flap + np.multiply(self.learn_rate * (target - Q_s[a]), phi)
        else:
            Q_s[a] = self.theta_noflap.dot(phi)
            self.theta_noflap = self.theta_noflap + np.multiply(self.learn_rate * (target - Q_s[a]), phi)

        print("flap:", self.theta_flap)
        print("noflap:", self.theta_noflap)
        print("Q[a]:", Q_s[a])
        print()
