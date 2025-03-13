## 1. Objectives

Feedforward Neural Networks, Back-propagation, and Stochastic Gradient Descent

Objectives:

- Write down recursive relations with **back-propagation algorithm** to compute the gradient of the loss function with respect to the weight parameters.
    
- Use the **stochastic descent algorithm** to train a feedforward neural network.
    
- Understand that it is not guaranteed to reach global (only local) optimum with SGD to minimize the training loss.
    
- Recognize when a network has **overcapacity**.
    

## 2. Back-propagation algorithm

How to evaluate the the gradient (the derivative of the loss)?

## 3. Training Model with 1 hidden Layer

Summary:

- For multi-layer neural networks, stochastic gradient descent (SGD) is not guaranteed to reach a global optimum
    
- Overcapcity help optimization
    
    - Larger models tend to be easier to learn because their units only need to be adjusted so that they are, collectively, sufficient to solve the task
    - Overcapicty (= number of units vs. dimension)
- Initialization has a role to find a good solution during training of neural networks
    
    - Randomization of initialization parameters give smoothness