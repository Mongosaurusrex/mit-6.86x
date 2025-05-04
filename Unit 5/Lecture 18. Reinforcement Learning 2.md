## Revisiting MDP Fundamentals

T(s,a,s'): "transition probability, the only thing that matters is the state you are in. It doesn't matter how you arrive, what you did before." = independent of the states visited before.  
R(s,a,s'): same.

$\pi^*$ s the optimal policy which record the actions leading to the best total reward/utility (from next step, and the following until the end), not the best immediate reward (for the next step only).

In the real world, $T$ and $R$ are unknown a-priori, so RL MDP algo starts with $<S,A>$ and learn them while exploring.

## Estimating Inputs for RL algorithm

Estimating Transition Probabilities and Rewards

#### Option 1:
With all data
$$
\hat{T} = \frac{ count(s,a,s') }{ \sum_{s'} count(s,a,s')}
$$
$\hat{T}$ is the number of actions leading to $s'$ over the total of actions

Issues:
- Certain states might not be visited at all while exploring
- Certain states might be visited much less often than others leading to noisy estimates

#### Option 2:
Model based approach first tries to estimate the probability distribution before estimating the expectation

## Q value iteration by sampling
$$sample_1: R(s,a,s_1') + \gamma max_{a'} Q(s_1',a')$$
$$\dots$$
$$sample_k: R(s,a,s_k') + \gamma max_{a'} Q(s_k',a')$$
And then average it:
$$Q(s,a) = {1 \over k} \sum_i^k sample_i = {1 \over k} \sum_i^k (R(s,a,s_i') + \gamma max_{a'} Q(s_i',a'))$$
#### The algorithm:
(1) Initialize the starting reward for the state
(2) Iterate until convergence
	(2.1) $Q_{i+1}(s,a) = \alpha * [ R(s,a,s') + \gamma max_{a'} Q(s', a')] + (1- \alpha) * Q_i(s,a)$
	(2.2) Convergence?


## Exploration vs Exploitation

$\epsilon$-greedy approach tries to balance exploration and exploitation:
- By randomly sampling an action with probability $\epsilon$
- and by choosing the best currently available option with probability $1-\epsilon$
$\epsilon$ (thus exploration) should decrease step by step over the trainings progress