#https://towardsdatascience.com/value-iteration-to-solve-openai-gyms-frozenlake-6c5e7bf0a64d

def TD_0(policy):
  #input policy=policy to be evaluated
  V = np.zeros(env.env.nS)
  for i in range(100):
    #initialize S
    S = env.reset()
    v=0 
    #loop for each step of episode
    for t in range(1000):
      # demo purposes always take random action
      A = int(np.random.rand()*len(policy[S]))
      # take action A observe outcome
      obs, reward, done, info = env.step(A)
      # sample expected values using Belman Optimality Update rule
      v += policy[S][A] * info['prob'] * (reward + 0.9 * V[obs])
      # use the current estimate instead of true value
      V[S] = v
      # check if episode is over
      if done:
        break
      # update value for none terminal states
      else:
        V[S] += V[S] + 0.001 * (reward + 0.9 * V[obs] - V[S])
        # update the state
        S = obs
  return V
  

def random_policy():
    return env.action_space.sample()




  
if __name__ =="__main__":
    # library imports
    import gym, numpy as np  #openAI gym 
    # gym environment
    gym.make('FrozenLake-v1', desc=None,map_name="4x4", is_slippery=True)
    #env=gym.make("FrozenLake-v0")
    # environment model
    env.env.P
    
    #dictionary of states
    V = {}
    for s in range(env.observation_space.n):
        V[s] = 0.0

    alpha = 0.85 #learning rate
    gamma = 0.90 #discount factor 
    
    #num episodes, timesteps
    num_episodes = 5000
    num_timesteps = 1000
    
    #for each episode
for i in range(num_episodes):
    s = env.reset() #initialize the state by resetting the environment
    print("resett env"+str(t))
    for s in range(env.observation_space.n):
        V[s] = 0.0
    for t in range(num_timesteps): #for every step in the episode
        #select an action according to random policy
        a = random_policy()
        #perform the selected action and store the next state information
        s_, r, done, _ = env.step(a)
        #compute the value of the state
        V[s] += alpha * (r + gamma * V[s_]-V[s])
        #update next state to the current state
        s = s_
        #if the current state is the terminal state then break
        if done:
            break
            


    df = pd.DataFrame(list(V.items()), columns=['state', 'value'])

            
    
    


