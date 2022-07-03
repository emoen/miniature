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
  
  
  
  
if __name__ =="__main__":
    # library imports
    import gym, numpy as np  #openAI gym 
    # gym environment
    env=gym.make("FrozenLake-v0")
    # environment model
    env.env.P