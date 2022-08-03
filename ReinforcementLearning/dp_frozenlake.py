#dynamic programming to get exact state-action values for frozen lake
#https://github.com/xadahiya/frozen-lake-dp-rl/blob/master/Dynamic_Programming_Solution.ipynb

# data science packages
import gym
import numpy as np
import pandas as pd
import plotnine as p9
import matplotlib.pyplot as plt
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

env = gym.make('FrozenLake-v1', desc=None,map_name="4x4", is_slippery=False)

def policy_evaluation(env, policy, gamma=1, theta=1e-8):
    V = np.zeros(env.observation_space.n)
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
    return V
    
random_policy = np.ones([env.observation_space.n, env.action_space.n]) / env.action_space.n 

V = policy_evaluation(env, random_policy)

plot_values(V)  
ax = sns.heatmap(V.reshape(4,4), annot=v, linewidth=0.5)
plt.show()

check_test.run_check('policy_evaluation_check', policy_evaluation)

policy_pi, V_pi = policy_iteration(env, gamma = 1, theta=1e-9, verbose = False)
plot_values(V_pi)