#https://marcinbogdanski.github.io/rl-sketchpad/RL_An_Introduction_2018/0403_Policy_Iteration.html

# Naive implementation (for loops are slow), but matches the box
def policy_iter(env, gamma, theta):
    """Policy Iteration Algorithm
    
    Params:
        env - environment with following required memebers:
            env.nb_states - number of states
            env.nb_action - number of actions
            env.model     - prob-transitions and rewards for all states and actions, see note #1
        gamma (float) - discount factor
        theta (float) - termination condition
    """
    
    # 1. Initialization
    V = np.zeros(env.nb_states)
    pi = np.zeros(env.nb_states, dtype=int)  # greedy, always pick action 0
    
    while True:
    
        # 2. Policy Evaluation
        while True:
            delta = 0
            for s in range(env.nb_states):
                v = V[s]
                V[s] = sum_sr(env, V=V, s=s, a=pi[s], gamma=gamma)
                delta = max(delta, abs(v - V[s]))
            if delta < theta: break

        # 3. Policy Improvement
        policy_stable = True
        for s in range(env.nb_states):
            old_action = pi[s]
            pi[s] = np.argmax([sum_sr(env, V=V, s=s, a=a, gamma=gamma)  # list comprehension
                               for a in range(env.nb_actions)])
            if old_action != pi[s]: policy_stable = False
        if policy_stable: break
    
    return V, pi
    
def sum_sr(env, V, s, a, gamma):
    """Calc state-action value for state 's' and action 'a'"""
    tmp = 0  # state value for state s
    for p, s_, r, _ in env.model[s][a]:     # see note #1 !
        # p  - transition probability from (s,a) to (s')
        # s_ - next state (s')
        # r  - reward on transition from (s,a) to (s')
        tmp += p * (r + gamma * V[s_])
    return tmp

import numpy as np
import matplotlib.pyplot as plt
import gym

env = gym.make('FrozenLake-v0')
env.reset()
env.render()

if not hasattr(env, 'nb_states'):  env.nb_states = env.env.nS
if not hasattr(env, 'nb_actions'): env.nb_actions = env.env.nA
if not hasattr(env, 'model'):      env.model = env.env.P

#do policy iteration
V, pi = policy_iter(env, gamma=1.0, theta=1e-8)
print(V.reshape([4, -1]))

#show optimal policya2w = {0:'<', 1:'v', 2:'>', 3:'^'}
policy_arrows = np.array([a2w[x] for x in pi])
print(np.array(policy_arrows).reshape([-1, 4]))

correct_V = np.array([[0.82352941, 0.82352941, 0.82352941, 0.82352941],
                      [0.82352941, 0.        , 0.52941176, 0.        ],
                      [0.82352941, 0.82352941, 0.76470588, 0.        ],
                      [0.        , 0.88235294, 0.94117647, 0.        ]])
correct_policy_arrows = np.array([['<', '^', '^', '^'],
                                  ['<', '<', '<', '<'],
                                  ['^', 'v', '<', '<'],
                                  ['<', '>', 'v', '<']])
assert np.allclose(V.reshape([4,-1]), correct_V)
assert np.alltrue(policy_arrows.reshape([4,-1]) == correct_policy_arrows)    