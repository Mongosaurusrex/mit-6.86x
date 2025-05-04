Reinforcement learning (RL) is a type of machine learning where an agent learns to make decisions by interacting with an environment. Instead of being given correct answers upfront (like in supervised learning), the agent receives feedback in the form of rewards or penalties based on its actions. Over time, the agent tries to learn a strategy, or policy, that maximizes its total reward. This is different from supervised learning, where a model is trained on a dataset of input-output pairs — for example, images labeled with the correct category — and learns to map inputs directly to correct outputs. In reinforcement learning, the correct action may not be obvious immediately, and the agent has to explore and learn from trial and error, making the problem more dynamic and sequential compared to supervised learning.

## Reinforcement Learning Terminology
A **Markov decision process (MDP)** is defined by

- 1. a set of states $s\in S$
- 2. a set of actions $a \in A$
- 3. Action dependent transition probabilities $T(a,s,s') = P(s' | s,a)$, so that for each state $s$ and action $a$, $\sum_{s' \in S} T(a,s,s') = 1$
- 4. Reward functions $R(s,a,s')$ representing the reward for starting in state, taking action and ending up in state after one step. (The reward function may also depend only on s, or only a and s.)

MDPs satisfy the **Markov property** in that the transition probabilities and rewards depend only on the current state and action, and remain unchanged regardless of the history (i.e. past states and actions) that leads to the current state.

## Utility function

How to aggregate reward? Utility function

Issue: infinite number of reward Bound the utility function

We consider two different types of utility functions:

Option 1: Finite horizon based utility

#### Option 1: Finite horizon based utility

The utility function is the sum of rewards after acting for a fixed number $n$ steps. For example, in the case when the rewards depend only on the states, the utility function is
$$U[s_0,...,S_n] = \sum_{i=0}^n R(s_i)$$
In particular $U[s_0,...,S_{n+m}] = U[s_0,...,S_n]$ for any positive integer $m$

Issues: The outcome of action depends only to the state, but not to the time to arrive to this state.

### Option 2: (Infinite horizon) Discounted reward based utility

In this setting, the reward one step into the future is discounted by a factor $\gamma$, the reward two steps ahead by, and so on. The goal is to continue acting (without an end) while maximizing the expected discounted reward. The discounting allows us to focus on near term rewards, and control this focus by changing. For example, if the rewards depend only on the states, the utility function is
$$\begin{align}
   U &= R(s_0) + \gamma R(s_1) + \gamma^2 R(s_2) + ... \\
   &= \sum_{t=0}^n \gamma^t R(s_t)
   \end{align}$$
Bounding of Utility function:
$$
\begin{align}
U &= \sum_{t=0}^\infty \gamma^t R(s_t) \\
&\le R(s_{max}) \sum_{t=0}^\infty \gamma^t \\
&\le {R_{max} \over 1 - \gamma}
\end{align}$$

Where $R_{max}$ is the maximal reward obtainable in any state. Which makes the algorithm converge

The main problem for MDPs is to optimize the agent's behavior. To do so, we first need to specify the criterion that we are trying to maximize in terms of accumulated rewards. We will define an **utility function** and maximize its expectation.

## Policy and Value functions

 A **policy** is a function, noted $\pi$, $\pi : s \to a$, that assigns an action $\pi(s)$ to any state $s$.  
An **optimal policy** is the optimal action that you can take in a state, the action that maximise the expected utility (here: the expected discounted reward).  
The optimal policy is denoted $\pi^*$.

## Bellman Equations
1. The **value function**, $V^*$ is the (max) expected reward from starting at state $s$ and acting optimally: $$V^*(s) = max_{a \in A} Q^*(s,a) = Q^*(s, \pi^*(a)$$
2. The **Q-function** $Q^*$ is the expected reward from starting at state $s$, then acting with action $a$, and acting optimally afterwards:$$Q^*(s,a) = \sum_{s' \in S} T(s,a,s') (R(s,a,s') + \gamma V^*(s'))$$
Thus:
$$V^*(s) = max_{a \in A} Q^*(s,a)$$
$$V^*(s) = max_{a \in A} \sum_{s' \in S} T(s,a,s') (R(s,a,s') + \gamma V^*(s')) \text{, where } 0\le \gamma \lt 1$$

From homework nice to have:
$$V_B = 1 + \gamma \cdot V_C, \quad \text{where} \quad V_C = \frac{10(1 + \gamma)}{1 - \gamma^2}$$
