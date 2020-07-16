from montecarlo_agent import MonteCarloAgent
from q_learning_agent import QLearningAgent
from function_approximation import FunctionAgent
from montecarlo_agent_best import MonteCarloAgentBest
from ple.games.flappybird import FlappyBird
from ple import PLE
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import time
import os

reward_values = {"positive": 1.0, "negative": 0.0, "tick": 0.0, "loss": -5.0, "win": 0.0}

def run_game(nb_episodes, agent, env, training):
    """ Runs nb_episodes episodes of the game with agent picking the moves.
        An episode of FlappyBird ends with the bird crashing into a pipe or going off screen.
    """
    scores = []
    score = 0
    while nb_episodes > 0:
        s1=env.game.getGameState()
        if training:
            action = agent.training_policy(s1)
        else:
            action = agent.policy(s1)

        # step the environment
        reward = env.act(env.getActionSet()[action])
        s2 = env.game.getGameState()

        if training:
            if reward==-5:
                agent.observe(s1,action,reward,s2,True)
            else:
                agent.observe(s1, action, reward, s2, False)    
            score += reward
        else:
            if reward == 1:
                score += 1
        
        # reset the environment if the game is over
        if env.game_over():
            print(agent.name, "score for this episode: %d" % score, nb_episodes)
            scores.append(score)
            env.reset_game()
            nb_episodes -= 1
            score = 0
    
    return scores

def run_training(episodes, agent):
    env = PLE(FlappyBird(), fps=30, display_screen=False, force_fps=True, rng=None,
          reward_values=reward_values)
    env.init()
    
    return run_game(episodes, agent, env, True)

def evaluate(episodes, agent):
    env = PLE(FlappyBird(), fps=30, display_screen=False, force_fps=True, rng=None,
          reward_values=reward_values)
    env.init()
    
    return run_game(episodes, agent, env, False)
    
def show_playing(episodes, agent):
    env = PLE(FlappyBird(), fps=30, display_screen=True, force_fps=False, rng=None,
      reward_values=reward_values)
    env.init()
    
    return run_game(episodes, agent, env, False)

def train_and_evaluate(train_per_ep, eval_per_ep, iterations, agent):
    evaluation_score = []
    for i in range (0, iterations):
        print("Iteration:", i+1)
        run_training(train_per_ep, agent)
        results = evaluate(eval_per_ep, agent)
        evaluation_score.append(results)
    return evaluation_score

#%%


def plot_average_score(scores, labels, colors, plot_std_dev):
    """
    Plot average score over episodes.
    scores: array of scores for an agent per iteration
    lables: array of names of agents (same indexing as scores)
    colors: colors for the plot
    """
    print("Plotting average scores ...")
    #Plot scores
    for i in range(len(scores)):
        avg = np.mean(scores[i], axis=1)
        avg = np.insert(avg, 0, 0)
        plt.plot(avg, label=labels[i], color=colors[i])

        if plot_std_dev:
            std_dev = np.asarray(np.std(scores[i], axis=1))
            std_dev = np.insert(std_dev, 0, 0)

            lower_bound = avg - std_dev
            upper_bound = avg + std_dev
            lower_bound[lower_bound < 0] = 0
            plt.fill_between(np.arange(len(avg)), lower_bound, upper_bound, alpha=0.2, color=colors[i])
      
    name = "_".join(labels)
    
    train_count = nb_iterations * nb_episodes
    x_ticks_count = 5
    
    # Change x axis values to go from 0 to number of training episodes
    plt.xticks(np.arange(0, nb_iterations + 1, nb_iterations / x_ticks_count), 
        np.arange(0, train_count + 1, int(train_count / x_ticks_count)),
        rotation=270)
    plt.title("Average score for " + name)
    plt.legend()
    if plot_std_dev:
        sd = "std_"
    else:
        sd = ""
    plt.savefig(folder_name + "/average_" + sd + name + "_" + str(nb_episodes * nb_iterations) + "ep.jpg");
    plt.clf()

#%%
def plot_qvalue_and_policy(Q_table, policy_table, agent_name):
    print("Plotting q values and policy for", agent_name, "...")
    table_x = 15
    table_y = 29
    add_const = 14
    # plot_table: [i - j, k, [q_flap], [q_noflap]]
    sa_table = [[[[], []] for _ in range(table_x)] for _ in range(table_y)]
    p_table = [[[] for _ in range(table_x)] for _ in range(table_y)]
    for i in range(0, 15): # player_y
        for j in range(0, 15): # next_pipe_top_y
            index = j - i + add_const
            for k in range(0, 15): # next_pipe_dist_to_player
                for l in range(0, 19): # player_vel
                    sa_table[index][table_x - k - 1][0].append(Q_table[i][j][k][l][0])
                    sa_table[index][table_x - k - 1][1].append(Q_table[i][j][k][l][1])
                    if len(policy_table) > 0:
                        p_table[index][table_x - k - 1].append(policy_table[i][j][k][l])
    

    for ij in range(len(sa_table)):
        for kt in range(len(sa_table[ij])):
            avg_q_flap = sum(sa_table[ij][kt][0]) / float(len(sa_table[ij][kt][0]))
            avg_q_noflap = sum(sa_table[ij][kt][1]) / float(len(sa_table[ij][kt][1]))            
            sa_table[ij][kt] = max(avg_q_flap, avg_q_noflap)
            if len(policy_table) > 0:
                p_table[ij][kt] = sum(p_table[ij][kt]) / float(len(p_table[ij][kt]))

    plt.figure(figsize=(12, 8))
    sns.heatmap(sa_table, annot=True, fmt=".2f")
    plt.xticks(np.arange(0.5, table_x, 1), np.arange(table_x - 1, -1, -1))
    plt.yticks(np.arange(0.5, table_y, 1), np.arange(table_y - add_const - 1, -add_const - 1, -1), rotation=0)
    plt.xlabel("Distance to the next pipe")
    plt.ylabel("next_pipe_top_y - player_y")
    plt.title("Values of the states after " + str(nb_episodes * nb_iterations) + " episodes for " + agent_name)
    plt.savefig(folder_name + "/" + agent_name + "_q_" + str(nb_episodes * nb_iterations) + "ep.jpg");

    if len(policy_table) > 0:
        plt.figure(figsize=(12, 8))
        sns.heatmap(p_table, annot=True, fmt=".2f")
        plt.xticks(np.arange(0.5, table_x, 1), np.arange(table_x - 1, -1, -1))
        plt.yticks(np.arange(0.5, table_y, 1), np.arange(table_y - add_const - 1, -add_const - 1, -1), rotation=0)
        plt.xlabel("Distance to the next pipe")
        plt.ylabel("next_pipe_top_y - player_y")
        plt.title("Policy after " + str(nb_episodes * nb_iterations) + " episodes for " + agent_name)
        plt.savefig(folder_name + "/" + agent_name + "_p_" + str(nb_episodes * nb_iterations) + "ep.jpg");
#%%
agent164 = MonteCarloAgent()
agent164.pipeDist = 164

agent164.name = "MonteCarlo"
agent164.discount = 0.9

agentQ283 = QLearningAgent()
agentQ283.name = "Q-learning"

agentBest = MonteCarloAgentBest()
agentBest.name = "MonteCarloBest"

nb_episodes = 5
nb_episods_eval = 5
nb_iterations = 3

s164 = train_and_evaluate(nb_episodes, nb_episods_eval, nb_iterations, agent164)
sq283 = train_and_evaluate(nb_episodes, nb_episods_eval, nb_iterations, agentQ283)
sb = train_and_evaluate(nb_episodes, nb_episods_eval, nb_iterations, agentBest)


time_started = time.strftime("%Y-%m-%d_%H-%M-%S")
folder_name = os.path.join("outputs", "out_" + time_started + "_" + str(nb_episodes * nb_iterations) + "ep") 
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print("folder name:", folder_name)

#%%
plot_average_score([s164, sq283], ['MonteCarlo', 'Q-learning'], ["blue", "orange"], True)
plot_average_score([s164], ["MonteCarlo"], ["blue"], True)
plot_average_score([sq283], ["Q-learning"], ["orange"], True)
plot_average_score([sb], ["MonteCarloBest"], ["black"], True)
plot_average_score([sb, s164], ["MonteCarloBest", "MonteCarlo"], ["black", "blue"], True)

plot_average_score([s164, sq283], ['MonteCarlo', 'Q-learning'], ["blue", "orange"], False)
plot_average_score([s164], ["MonteCarlo"], ["blue"], False)
plot_average_score([sq283], ["Q-learning"], ["orange"], False)
plot_average_score([sb], ["MonteCarloBest"], ["black"], False)
plot_average_score([sb, s164], ["MonteCarloBest", "MonteCarlo"], ["black", "blue"], False)

plot_qvalue_and_policy(agent164.Q_table, agent164.get_policy_table(), agent164.name)
plot_qvalue_and_policy(agentQ283.Q_table, agentQ283.get_policy_table(), agentQ283.name)
plot_qvalue_and_policy(agentBest.Q_table, agentBest.get_policy_table(), agentBest.name)

print("Plots saved to folder /" + folder_name)

# It's play time!
num_repeat = 1
while num_repeat > 0:
    num_repeat = input("How many times do you want to see me play? (enter 0 to end)\n")
    if (not num_repeat.isdigit()):
        print("That is not a number!")
        num_repeat = 1
        continue
    num_repeat = int(num_repeat)
    show_playing(num_repeat, agent164)
    show_playing(num_repeat, agentQ283)
    show_playing(num_repeat, agentBest)

"""
agentFunc = FunctionAgent()
out = run_training(6, agentFunc)
"""
