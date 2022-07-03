### Temporal-Difference Learning (TD)

Both TD and Monte Carlo use experience to solve prediction problem. Following policy pi, 
both methods update their estimates V of pi_v for non-terminal state S._t
Monte Carlo wait until the return following the visit is know, then use that return
as a target for V(S_t):

A simple every-visit MC:

V(S_t) = V(S_t) + alpha[G_t - V(S_t)], alpha is a constant. Lets call this alpha-MC.

G_t is the actual return following time t. MC methods must wait until G_t is know to update V(S_t), 
TD methods need only wait until next time-step. 
At time t+1 they for a target, and make an update using 
observed reward R_t+1 and the estimate V(S_t+1). TD update becomes

V(S_t) = V(S_t) + alpha[R_t+1 + gamma*V(S_t+1)-v(S_t)] 

imediatly on transition S_t and receives R_t+1. For MC the target is G_t and
for TD it is R_t+1 + gamma*V(S_t+1). Gamma is the discount factor.
This method is called TD(0) - one step TD.

def tabular_TD_0_to_estimate_V_pi(pi, alpha:(0,1]):
  initialize V(S), for all s in S+, except V(terminal)=0
  for each step in episode and S != terminal:
    A = action given pi for S
	Take action A, observe R, S'
	V(S) = V(S) + alpha[R+ gamma*V(S')-V(S)]
	S = S'