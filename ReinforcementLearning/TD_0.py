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

    # num episodes, timesteps
gamma = 0.90  # discount factor    
alpha = 0.85  # learning rate
num_episodes = 100000
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
#https://www.geeksforgeeks.org/sarsa-reinforcement-learning/


#Function to choose the next action
def choose_action(state): #eps-greedy
    action=0
    if np.random.uniform(0, 1) < epsilon: #with probability 1-epsilon do random move
        action = env.action_space.sample()
    else:
        action = np.argmax(Q[state, :])
    return action
 
#Function to learn the Q-value
def update(s, s2, reward, a, a2): #sarsa
    predict = Q[s, a]
    if s==13 and a==2:
        tmp_target = reward + gamma * Q[s2, a2]
        #print(str( Q[s,a] ) + " "+ str( Q[s, a] + alpha * (tmp_target - predict) )+ " next state action:"+str(s2)+" "+str(a2)+ " "+str(Q[14,:]) )
    target = reward + gamma * Q[s2, a2]
    Q[s, a] = Q[s, a] + alpha * (target - predict)
    
#Function to learn the Q-value
def q_update(s, s2, reward, a): #Q-learning
    predict = Q[s, a]
    if s==13 and a==2:
        tmp_target = reward + gamma * np.max( Q[s2, :] )
        #print(str( Q[s,a] ) + " "+ str( Q[s, a] + alpha * (tmp_target - predict) )+ " next state action:"+str(s2)+" "+str(a2)+ " "+str(Q[14,:]) )
    target = reward + gamma * np.max( Q[s2, :] )
    Q[s, a] = Q[s, a] + alpha * (target - predict)    


epsilon = 0.1
Q = np.zeros((env.observation_space.n, env.action_space.n)) # Q matrix

#Initializing the reward
reward=0

#0: LEFT 1: DOWN 2: RIGHT 3: UP
# Starting the SARSA learning
VV = np.zeros(num_episodes*num_timesteps)
VV13 = np.zeros(num_episodes*num_timesteps)
VV10 = np.zeros(num_episodes*num_timesteps)
counter = 0
for episode in range(num_episodes):
    t = 0
    s1 = env.reset()
    
    a1 = choose_action(s1) #sarsa
 
    while t < num_timesteps:
        a1 = choose_action(s1) #Q-learning
        
        #env.render() #Visualizing the training
         
        #Getting the next state
        s2, reward, done, info = env.step(a1)
 
        #Choosing the next action
        a2 = choose_action(s2) #sarsa
         
        #Learning the Q-value
        #update(s1, s2, reward, a1, a2) #sarsa
        q-update(s1, s2, reward, a1)    #Q-learning
 
        s1 = s2
        a1 = a2 #sarsa
         
        #Updating the respective vaLues
        t += 1
        reward += 1
        
        VV10[counter] = Q[10,1] # 10 step and step down    
        VV13[counter] = Q[13, 2] # 13 step and step right    
        VV[counter] = Q[14, 2] # last step and step right        
        counter +=1
        
        #If at the end of learning process
        if done:
            break
    
print(counter)
    
plt.plot(VV[0:counter])
plt.show()     

plt.plot(VV13[0:counter])
plt.show()    

plt.plot(VV10[0:counter])
plt.show()    

np.set_printoptions(suppress=True)

# Starting the Q-learning learning
VV = np.zeros(num_episodes*num_timesteps)
VV13 = np.zeros(num_episodes*num_timesteps)
VV10 = np.zeros(num_episodes*num_timesteps)
counter = 0
for episode in range(num_episodes):
    t = 0
    s1 = env.reset()
 
    while t < num_timesteps:
        a1 = choose_action(s1) #Q-learning
        s2, reward, done, info = env.step(a1) #Getting the next state   
        q_update(s1, s2, reward, a1)    #Q-learning
 
        s1 = s2
        t += 1         #Updating the respective vaLues
        reward += 1
        
        VV10[counter] = Q[10,1] # 10 step and step down    
        VV13[counter] = Q[13, 2] # 13 step and step right    
        VV[counter] = Q[14, 2] # last step and step right        
        counter +=1
        
        if done: #If at the end of learning process
            break

plt.plot(VV[0:counter])
plt.show()     

plt.plot(VV13[0:counter])
plt.show()    

plt.plot(VV10[0:counter])
plt.show() 