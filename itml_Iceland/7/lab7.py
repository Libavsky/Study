import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import random
from itertools import islice

# An abstract class representing a Markov Decision Process (MDP).
class MDP:
    def __init__(self):
        self.computeStates()

    # discount factor
    discountFactor = 1

    # Return the start state.
    def startState(self): raise NotImplementedError("Override me")

    # Return set of actions possible from |state|.
    def actions(self, state): raise NotImplementedError("Override me")

    # Return a list of (newState, prob, reward) tuples corresponding to edges
    # coming out of |state|.
    # Mapping to notation from class:
    #   state = s, action = a, newState = s', reward = r, prob = p(s', r | s, a)
    # If state is a terminal state, return the empty list.
    def succAndProbReward(self, state, action): raise NotImplementedError("Override me")

    # Compute set of states reachable from startState.  Helper function
    # to know which states to compute values and policies for.
    # This function sets |self.states| to be the set of all states.
    def computeStates(self):
        self.states = set()
        queue = []
        self.states.add(self.startState())
        queue.append(self.startState())
        while len(queue) > 0:
            state = queue.pop()
            for action in self.actions(state):
                for newState, prob, reward in self.succAndProbReward(state, action):
                    if newState not in self.states:
                        self.states.add(newState)
                        queue.append(newState)
                        #print(newState)
        print("%d reachable states" % len(self.states))
        
class BlackjackMDP(MDP):
    
    # the discount factor for future rewards
    discountFactor = 1 # TODO: set this to the correct value
    
    # Return the start state.
    def startState(self):
        # TODO: come up with some representation for states and return the initial state here
        return (0, False, 0, False, "start")

    # Return set of actions possible from |state|.
    def actions(self, state):
        # TODO: you may need to change this depending on your model
        #       not all actions may always be possible
        if state[4] == "player":
            return ["Hit", "Stand"]
        else:
            return ["Noop"]

    # Return a list of (newState, prob, reward) tuples corresponding to edges
    # coming out of |state|.
    # Mapping to notation from class:
    #   state = s, action = a, newState = s', reward = r, prob = p(s', r | s, a)
    # If state is a terminal state, return the empty list.
    def succAndProbReward(self, state, action):
        # TODO: implement this
        return_list = []
        if state[4] == "player" and action == "Hit":
            for card in range (2,12):
                usable_ace = state[1]
                pr_card = 4 / 52
                if card == 10:
                    pr_card = 16 / 52
                if card == 11:
                    if state[1] == False:
                        usable_ace = True
                    else:
                        card-=10
                if state[0]+card>21 and usable_ace==False:
                    new_state = (state[0] + card, False, state[2], state[3], "end")
                    return_list.append((new_state, pr_card, -1))
                elif state[0]+card>21 and usable_ace==True:
                    if state[0]+card-10>21:
                        new_state = (state[0] + card, False, state[2], state[3], "end")
                        return_list.append((new_state, pr_card, -1))
                    else:
                        new_state = (state[0]+card-10, False, state[2], state[3], "player")
                        return_list.append((new_state, pr_card, 0))
                elif state[0]+card<=21:
                    new_state = (state[0] + card, usable_ace, state[2], state[3], "player")
                    return_list.append((new_state, pr_card, 0))
        elif state[4] == "player" and action == "Stand":
            new_state = (state[0], state[1], state[2], state[3], "dealer")
            return_list.append((new_state, 1, 0))
        elif state[4] == "dealer":
            usable_ace = state[3]
            if state[2]>=17:
                x = 0
                if state[0]>state[2]:
                    x=1
                elif state[0]<state[2]:
                    x=-1
                new_state = (state[0], state[1], state[2], state[3], "end")
                return_list.append((new_state, 1, x))
                return return_list
            for card in range (2,12):
                pr_card = 4 / 52
                if card == 10:
                    pr_card = 16 / 52
                if card == 11:
                    if state[3] == False:
                        usable_ace = True
                    else:
                        card-=10
                if state[2]+card>21 and usable_ace==False:
                    new_state = (state[0], state[1], state[2]+card, usable_ace, "end")
                    return_list.append((new_state, pr_card, 1))
                elif state[2]+card>21 and usable_ace==True:
                    if state[2]+card-10>21:
                        new_state = (state[0], state[1], state[2] + card, usable_ace, "end")
                        return_list.append((new_state, pr_card, 1))
                    else:
                        new_state = (state[0], state[1], state[2]+card-10, False, "dealer")
                        return_list.append((new_state, pr_card, 0))
                elif state[2]+card<=21:
                    new_state = (state[0], state[1], state[2]+card, usable_ace, "dealer")
                    return_list.append((new_state, pr_card, 0))
        elif state[4] == "start":
            for first in range(2, 12):
                usable_ace = False
                pr_first = 4/52
                if first == 10:
                    pr_first = 16/52
                if first == 11:
                    usable_ace = True
                for second in range(2, 12):
                    tmp_value = first + second
                    pr_second = 4/52
                    if second == 10:
                        pr_second = 16/52
                    if second == 11:
                        if usable_ace:
                            tmp_value -= 10
                        usable_ace = True

                    for third in range(2, 12):
                        pr_third = 4/52
                        if third == 10:
                            pr_third = 16/52
                        usable_ace_dealer = False
                        if third == 11:
                            usable_ace_dealer = True
                        probability = pr_first * pr_second * pr_third
                        new_state = (tmp_value, usable_ace, third, usable_ace_dealer, "player")
                        return_list.append((new_state, probability, 0))
        elif state[4] == "end":
            #return_list.append((self.terminalState, 1, 0))
            return []
        return return_list

    def simulateGame(self):
        state = self.startState()
        print(state)
        while state[4] != "end":
            possible_actions = self.actions(state)
            action = possible_actions[random.randint(0, len(possible_actions) - 1)]
            print("Selected action:", action)
            possible_states = self.succAndProbReward(state, action)
            selected_random_state = possible_states[random.randint(0, len(possible_states) - 1)]
            print(selected_random_state)
            state = selected_random_state[0]

def V(mdp, v, state, action):
    possible_states = mdp.succAndProbReward(state, action)
    value = 0
    for pos_state in possible_states:
        value += pos_state[1] * (pos_state[2] + mdp.discountFactor * v[pos_state[0]])
    
    return value

def valueIteration(mdp):
    large_negative_number = -1000000000
    v = {}
    for state in mdp.states:
        v[state] = 0
    
    # do actual value iteration
    theta = 0.0000000000000001
    delta = 2 * theta # any value, but it should be greater than theta

    while delta > theta:
        delta = 0
        for state in mdp.states:
            vv = v[state]
            maxi = large_negative_number
            for action in mdp.actions(state):
                maxi = max(maxi, V(mdp, v, state, action))
            v[state] = maxi
            delta = max(delta, abs(vv - v[state]))


    pi = {}

    # extract policy
    for state in mdp.states:
        maxi = large_negative_number
        best_action = None
        for action in mdp.actions(state):
            val = V(mdp, v, state, action)
            if val > maxi:
                maxi = val
                best_action = action
        pi[state] = best_action
            


    return (v, pi)

mdp = BlackjackMDP()
for i in range(1,11):
    print("\nSimulate game #" + str(i))
    mdp.simulateGame()


viter = valueIteration(mdp)

print("\nValue iteration")
for state, reward in list(islice(viter[0].items(), 20)):
    print(state, reward)

print("\nBest policy")
for state, action in list(islice(viter[1].items(), 20)):
    print(state, action)

# Part 2.b)
print("\nStart state value:", viter[0][mdp.startState()])

#%%
def report_value(mdp):
    playerTrue = []
    playerFalse = []
    for state, action in viter[0].items():
        if state[4] == "player":
            if state[1] == True:
                playerTrue.append([state[0], state[2], action])
            else:
                playerFalse.append([state[0], state[2], action])
                
    plot_value(playerTrue, "Player has an usable ace")
    plot_value(playerFalse, "Player doesn't have an usable ace")

def plot_value(orig_data, title):
    data = pd.DataFrame(orig_data)
    data = data.pivot(0, 1, 2)    
    
    ax = plt.axes()
    ax.set_title(title)
    hm = sns.heatmap(data, annot=True, fmt='.3f', ax=ax)
    
    hm.set_ylabel("Player sum")
    hm.set_xlabel("Dealer showing")
    plt.show()
    
report_value(mdp)
#%%
def report_policy(mdp):
    playerTrue = []
    playerFalse = []
    for state, action in viter[1].items():
        if state[4] == "player":
            if state[1] == True:
                playerTrue.append([state[0], state[2], action])
            else:
                playerFalse.append([state[0], state[2], action])

    plot_policy(playerTrue, "Player has an usable ace",
                (8,3))
    plot_policy(playerFalse, "Player doesn't have an usable ace",
                (8,5))
        
def plot_policy(orig_data, title, figsize):
    orig_data.sort()
    min_player = orig_data[0][0]
    max_player = orig_data[len(orig_data)-1][0]
    min_dealer = orig_data[0][1]
    max_dealer = orig_data[len(orig_data)-1][1]
    
    column_count = max_dealer - min_dealer + 1
    row_count = max_player - min_player + 1
    
    cell_data = []
    
    #Initialize table
    for i in range (0, row_count):
        new_row = [[]] * column_count
        cell_data.append(new_row)
    
    #Set values of cells
    for state in orig_data:
        row = state[0] - min_player
        column = state[1] - min_dealer
        cell_data[row][column] = state[2]
        
        
    columns = np.arange(min_dealer, max_dealer + 1, 1)
    rows = np.arange(min_player, max_player + 1, 1)
    
    fig, ax = plt.subplots(figsize=figsize)
    
    plt.title(title)
    ax.axis('off')
    ax.axis('tight')
    
    # Add colors
    colors = [[[0] for _ in range(len(cell_data[0]))] for _ in range(len(cell_data))]
    for y in range(len(colors)):
        for x in range(len(colors[0])):
            if (cell_data[y][x] == 'Hit'):
                colors[y][x] = '#FFB84F'
            else:
                colors[y][x] = '#6EC2FF'
    
    ax.table(cellText=cell_data,
              rowLabels=rows,
              colLabels=columns,
              loc='center',
              cellLoc='center',
              cellColours=colors)

    plt.show()


report_policy(mdp)
