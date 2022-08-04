#dynamic programming to get exact state-action values for frozen lake
#https://github.com/xadahiya/frozen-lake-dp-rl/blob/master/Dynamic_Programming_Solution.ipynb

# data science packages
import gym
import numpy as np
import pandas as pd
import plotnine as p9
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

# RL algorithms
from qlearning import *
from dp import *

# utils
from helpers import *
from plot_utils import plot_values
import copy
import dill

from frozenlake import FrozenLakeEnv

import imageio

env = gym.make('FrozenLake-v1', desc=None,map_name="4x4", is_slippery=False)

filenames = []
def policy_evaluation(env, policy, gamma=1, theta=1e-4):
    V = np.zeros(env.observation_space.n)
    i =0
    while True:
        delta = 0
        for s in range(env.observation_space.n):
            Vs = 0
            for a, action_prob in enumerate(policy[s]):
                for prob, next_state, reward, done in env.P[s][a]:
                    Vs += action_prob * prob * (reward + gamma * V[next_state])
            delta = max(delta, np.abs(V[s]-Vs))
            V[s] = Vs
        if delta < theta:
            break
        
        # create file name and append it to a list
        if i < 15:
            filename = f'{i}.png'
            filenames.append(filename)
            i+=1
        
        
        #plt.ion() #ioff()
        ax = sns.heatmap(V.reshape(4,4), annot=True, linewidth=0.5, cbar=False)
        
        plt.draw()
        
        if i < 15:
            plt.savefig(filename)
        
        plt.pause(0.5)
        
        plt.clf()
        sns.heatmap(V.reshape(4,4), annot=False, linewidth=0.5, cbar=False)
        plt.draw()
        plt.pause(0.1)
        
        
    # build gif
    with imageio.get_writer('mygif.gif', mode='I', fps=1) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
            
    # Remove files
    for filename in set(filenames):
        os.remove(filename)
    return V
    
random_policy = np.ones([env.observation_space.n, env.action_space.n]) / env.action_space.n 

V = policy_evaluation(env, random_policy)

