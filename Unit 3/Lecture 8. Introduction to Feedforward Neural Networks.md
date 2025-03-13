At the end of this lecture, you will be able to

- Recognize different **layers** in a **feedforward neural network** and the number of **units** in each layer.
    
- Write down common **activation functions** such as the hyperbolic tangent function , and the **rectified linear function (ReLU)** .
    
- Compute the output of a simple neural network possibly with **hidden layers** given the **weights** and **activation functions** .
    
- Determine whether data after transformation by some layers is linearly separable, draw decision boundaries given by the weight vectors and use them to help understand the behavior of the network.
## Motivation
![[Pasted image 20250304162626.png]]
So far, we have treated classification as a task where a given set of pre-compiled features (represented as a feature vector) is used in a linear decision rule with weights  $\theta$  to make predictions. However, in a feedforward neural network, instead of relying on pre-defined features, the network learns the feature representation $\phi(x)$  dynamically while optimizing  $\theta$  to achieve the best classification performance.

## Neural Network Units
A neural netrowk unit is a primitive neural network that consists of only the "input layer", and an output layer with only one output. It is represented pictorially:
![[Pasted image 20250304164301.png]]
A neural network unit computes a non-linear weighted combination of its input:
$$
\hat y = f(z),\ where \ z=w_0+\sum_{i=1}^dx_iw_i
$$
Where $w_i$ are numbers called weights, $z$ is a number and is the weighted sum of the inputs $x_i$, and $f$ is generally a non-linear function called the activation function

The above equation in vector form is:
$$
\hat y = f(z)\ where\ z = w_0+x\cdot w
$$
where $x = [x_1,\dots,x_d]$ and $w=[w_1,\dots,w_d]^T$

### Examples
![[Pasted image 20250304164845.png]]
$$
z = w_0+x\cdot w = -2
$$
$$
\hat y = f(z) = max\{0,z\} = max\{0,-2\} = 0
$$
Because $f(z)$ is ReLU which $=max\{0,z\}$

## Motivation to deep neural networks

![[Pasted image 20250305152400.png]]

- Deep neural network
	- Loosely motivated by biological neurons, networks
	- Adjustable processing units ( ~ linear classifiers )
	- Highly parallel, typically organised in layers
	- Deep = many transformations (layers before output)

A **deep (feedforward) neural network** refers to a neural network that contains not only the input and output layers, but also hidden layers in between. For example, below is a deep feedfoward neural network of 2 hidden layers, with each hidden layer consisting of 5 units:

One of the main advantages of deep neural networks is that in many cases, they can learn to extract very complex and sophisticated features from just the raw features presented to them as their input. For instance, in the context of image recognition, neural networks can extract the features that differentiate a cat from a dog based only on the raw pixel data presented to them from images.  

The initial few layers of a neural networks typically capture the simpler and smaller features whereas the later layers use information from these low-level features to identify more complex and sophisticated features.

## Models with hidden layer
![[Pasted image 20250305154017.png]]
![[Pasted image 20250305154203.png]]
![[Pasted image 20250305154722.png]]
## Back-propagation Algorithm
![[Pasted image 20250306151639.png]]
![[Pasted image 20250306152134.png]]
![[Pasted image 20250306153208.png]]

Backpropagation is a key algorithm for training deep neural networks by efficiently computing gradients using the **chain rule**. It propagates the error from the output layer back through the network, updating weights to minimize the loss function. The process starts by computing the gradient of the loss with respect to the final layer’s output, typically using  $\frac{\partial \mathcal{L}}{\partial f_L} = -(y - f_L)$ **for squared error loss**. Then, for each hidden layer, the gradient is recursively computed as  $\delta_i = f{\prime}(z_i) w_{i+1} \delta_{i+1}$ , where  $f{\prime}$  is the derivative of the activation function and  $w_{i+1}$  is the weight of the next layer. Finally, the weight gradients are obtained using  $\frac{\partial \mathcal{L}}{\partial w_i} = x_i \cdot \delta_i$ , allowing weights to be updated using gradient descent. This recursive approach efficiently distributes error information, enabling deep networks to learn complex representations.

## Summary
- Neural Networks can be learned with SGD similarly to linear classifiers
- The derivatives necessary for SGD can be evaluated effectively via back-propagation
- Multi-layer neural network models are complicated we are no longer guaranteed to reach global optimum with SGD
- Larger models tend to be easier to learn ... units only need to be adjusted so that they are, collectively sufficient to solve the task
