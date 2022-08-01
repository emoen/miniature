

num_episodes = 100#0
num_timesteps = 1000

    
V = {}
for s in range(env.observation_space.n):
    V[s] = 0.0

for i in range(num_episodes):
    s = env.reset()  # initialize the state by resetting the environment
    V = doOne(V, env, s, num_timesteps, i)

    
def doOne(V, env, s, num_timesteps, episode):
    route = np.asarray([0])
    for t in range(num_timesteps): 
        a = random_policy()
        s_, r, done, _ = env.step(a)
        route = np.append(route, s_)
        tmp = V.copy()
        old = V[s]
        V[s] += alpha * (r + gamma * V[s_]-V[s])
        
        if( V!=tmp and round(V[s], 2)>=0.01):
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