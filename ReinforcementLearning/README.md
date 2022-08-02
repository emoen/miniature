### Temporal-Difference Learning (TD)

(policy iteration vs value iteration)

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

<pre>
def tabular_TD_0_to_estimate_V_pi(pi, alpha:(0,1]):
  initialize V(S), for all s in S+, except V(terminal)=0
  for each step in episode and S != terminal:
    A = action given pi for S
	Take action A, observe R, S'
	V(S) = V(S) + alpha[R+ gamma*V(S')-V(S)]
	S = S'
</pre>

### Step valuation under random policy

The second last step evaluation of frozen lake 4x4 under random policy:
<img src="https://github.com/emoen/miniature/blob/master/ReinforcementLearning/img/random_policy_td0.png" />


### Policy iteration - Sarsa: On-policy and Q-learning: off-policy

On-policy:
<pre>
def Sarsa(step_size_alpha in (0,1], epsilon > 0):
    initialize Q(s, a), for all s in S+, a in A(s), arbitrarily, except Q(terminal, .)=0
	for each episode:
	    initialize S
		Choose A from S using policy derived from Q (epsilon-greedy)
		loop for each step in episode:
		    take action A, observe R, S'
			choose A' from S' under policy derived from Q
			Q(S, A) = Q(S, A) + alpha*[R + gamma*Q(S', A') - Q(S, A)]
			S = S', A = A'
	    until S terminal
</pre>

Off-policy
<pre>
def Q-learning(step_size_alpha in (0,1], epsilon > 0):
    initialize Q(s, a) for all s in S+, a in A(s), arbitrarily, except Q(terminal, .)=0
	for each episode:
	    initialize S

		loop for each step in episode:
			Choose A from S using policy derived from Q (epsilon-greedy)
		    take action A, observe R, S'
			
			Q(S, A) = Q(S, A) + alpha*[R + gamma*Q(S', A') - Q(S, A)]
			S = S'
	    until S terminal
</pre>			


The second last step evaluation of frozen lake 4x4 under sarsa when action is go right:
<img src="https://github.com/emoen/miniature/blob/master/ReinforcementLearning/img/SARSA_last_step_go_right.png" />
