- derive non-linear classifiers from feature maps
    
- move from coordinate parameterization to weighting examples
    
- compute kernel functions induced from feature maps
    
- use kernel perceptron, kernel linear regression
    
- understand the properties of kernel functions

## Higher order feature vectors
![[Pasted image 20250222130426.png]]

• **Linear classifiers can be extended to capture more complex decision boundaries** by **mapping inputs to higher-dimensional feature spaces**.

• This method allows for **nonlinear classification** while still using a linear model in the transformed space.

• The choice of  $\phi(x)$  determines the shape of the decision boundary. Here, a quadratic term  $x^2$  allows the decision boundary to be a **parabola**.

![[Pasted image 20250222131247.png]]
![[Pasted image 20250222131512.png]]![[Pasted image 20250222132018.png]]

## Polynomial features
![[Pasted image 20250222133119.png]]
![[Pasted image 20250222133315.png]]
![[Pasted image 20250222133421.png]]
## Kernels
![[Pasted image 20250222135332.png]]
![[Pasted image 20250222135511.png]]

## The Kernel Perceptron Algorithm
![[Pasted image 20250224160825.png]]
**Key Takeaways**

• Instead of maintaining  $\theta$ , we store **support vectors** and their coefficients  $\alpha_j$ .

• The **kernel function**  $K(x^{(j)}, x^{(i)})$  replaces the explicit feature mapping  $\phi(x)$ .

• This enables the perceptron to work for **non-linearly separable** data efficiently.

## Kernel Composition rules
![[Pasted image 20250224163016.png]]



## Summary
- We can get non-linear classifiers or regression methods by simply mapping examples into feature vectors non-linearly and applying a linear method on the resulting vectors.
- These feature vectors can be high dimensional, however
- We Can turn the linear methods into kernel methods by casting the computations in terms of inne products
- A kernel funtion is simply an inner product between two feature vectors
- Using kernels is advantageous when the inner products are faster to evaluate than using explicit vectors
