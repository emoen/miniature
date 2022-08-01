#https://towardsdatascience.com/value-iteration-to-solve-openai-gyms-frozenlake-6c5e7bf0a64d

import gym
import pygame
import numpy as np
import matplotlib.pyplot as plt

def TD_0(policy): #input policy=policy to be evaluated
  V = np.zeros(env.env.nS)
  for i in range(100):
    S = env.reset()
    v=0 
    for t in range(1000): #steps in episode
      A = int(np.random.rand()*len(policy[S])) # demo purposes always take random action
      obs, reward, done, info = env.step(A)    # take action A observe outcome
      v += policy[S][A] * info['prob'] * (reward + 0.9 * V[obs]) # sample expected values using Belman Optimality Update rule
      V[S] = v                                 # use the current estimate instead of true value
      if done: # check if episode is over
        break
      
      else:    # update value for none terminal states
        V[S] += V[S] + 0.001 * (reward + 0.9 * V[obs] - V[S]) # update the state
        S = obs 
  return V
  

def random_policy():
    return env.action_space.sample()
    
    
#num_episodes = 100#0
#num_timesteps = 1000
  
#V = {}
#for s in range(env.observation_space.n):
#    V[s] = 0.0

#for i in range(num_episodes):
#    s = env.reset()  # initialize the state by resetting the environment
#    V = doOne(V, env, s, num_timesteps, i)

def doOne(V, env, s, num_timesteps, episode): #TD_0
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
    # library imports
    import gym, numpy as np  #openAI gym
    # gym environment
    env = gym.make('FrozenLake-v1', desc=None,map_name="4x4", is_slippery=False)
    #env=gym.make("FrozenLake-v0")
    # environment model
    env.env.P

    #df = pd.DataFrame(list(V.items()), columns=['state', 'value'])
    # dictionary of states
    V = {}
    for s in range(env.observation_space.n):
        V[s] = 0.0

    alpha = 0.85  # learning rate
    gamma = 0.90  # discount factor

    # num episodes, timesteps
num_episodes = 10000
num_timesteps = 1000

    # for each episode
V0 = np.zeros(num_episodes)
V13 = np.zeros(num_episodes)
for i in range(num_episodes):
    s = env.reset()  # initialize the state by resetting the environment
    V = doOne(V, env, s, num_timesteps, i)
    V0[i] = V[0]
    V13[i] = V[14]

plt.plot(V13)
plt.show()        
    
    


