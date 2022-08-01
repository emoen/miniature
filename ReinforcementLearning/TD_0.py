# ( https://towardsdatascience.com/value-iteration-to-solve-openai-gyms-frozenlake-6c5e7bf0a64d )
#https://medium.com/reinforcement-learning-in-python-temporal/reinforcement-learning-in-python-temporal-difference-prediction-5b3b4e46f22f

import gym
import pygame
import numpy as np
import matplotlib.pyplot as plt

def random_policy():
    return env.action_space.sample()

def TD_0(V, env, s, num_timesteps, episode): #TD_0
    debug = False
    route = np.asarray([0])
    for t in range(num_timesteps): 
        a = random_policy()
        s_, r, done, _ = env.step(a)
        route = np.append(route, s_)
        tmp = V.copy()
        old = V[s]
        V[s] += alpha * (r + gamma * V[s_]-V[s])
        
        if( V!=tmp and debug):
            printLake(V, route)
            print("************** timesteps:"+str(t)+ " episode:"+str(episode)+ " change:"+str(s)+", "+str(V[s]))
            print("************** r="+str(r)+" V[s_]="+str(V[s_])+" s_="+str(s_)+" V[s]="+str(old)+" "+str(s)+ " eq="+str(alpha * (r + gamma * V[s_]-old))+" "+str(gamma * V[s_]-old)+" "+str(gamma)+" "+str(gamma*V[s_]))
            
        s = s_
        if done:
            if (r > 0):
                print("###### DONE ######### timesteps:"+str(t)+ " episode:"+str(episode))
            break
    return V        

def printLake(V, route):
  print(route)
  routeLine = ["x"] * 16
  for i in range(0, len(V)):
    print( round( V[i], 2 ), end=" ")
    if ( len(np.where(route == i)[0]) > 0 ):
        routeLine[i] = str( len(np.where(route == i)[0]) ) 
    if ((i+1) % 4)== 0 :
        #print(" "+ str(i-3)+" "+str(i+1))
        print("\t", end=" ")
        print(" ".join(routeLine[i-3:i+1] ) )
        
if __name__ =="__main__":
    env = gym.make('FrozenLake-v1', desc=None,map_name="4x4", is_slippery=False)
    env.env.P

    #df = pd.DataFrame(list(V.items()), columns=['state', 'value']) # dictionary of states
    
V = {}
for s in range(env.observation_space.n):
    V[s] = 0.0


alpha = 0.85  # learning rate
gamma = 0.90  # discount factor

    # num episodes, timesteps
num_episodes = 10000
num_timesteps = 1000

    # for each episode
    
env = gym.make('FrozenLake-v1', desc=None,map_name="4x4", is_slippery=False)    
V0 = np.zeros(num_episodes)
V13 = np.zeros(num_episodes)
for i in range(num_episodes):
    s = env.reset()  # initialize the state by resetting the environment
    V = TD_0(V, env, s, num_timesteps, i)
    V0[i] = V[0]
    V13[i] = V[14]

plt.plot(V13)
plt.show()        
    
    
############### policy #########################


