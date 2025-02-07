
- understand the concepts of Feature vectors and labels, Training set and Test set, Classifier, Training error, Test error, and the Set of classifiers
    
- derive the mathematical presentation of linear classifiers
    
- understand the intuitive and formal definition of linear separation
    
- use the perceptron algorithm with and without offset
## Linear Classifiers Mathematically revisited
![[Pasted image 20250131131150.png]]
In the plane a linear classifier describes a split of the space with a decision boundary, where a prediction might look in one way on one side and look differently in another. We can have a set of classifiers and we need to define a set of classifiers in order to be able to determine the best of them.

![[Pasted image 20250131132135.png]]
$\theta$ defines the direction perpendicular to the decision boundary, splitting the space into two regions. The classifier uses the sign of the projection $(\theta^\top x)$ to determine which side of the boundary a point lies on, ensuring consistent classification. Orthogonality guarantees that \theta correctly aligns with the boundary for accurate separation of classes.

The line described by $\theta_1 x_1 + \theta_2 x_2 = 0$ comes directly from the definition of the decision boundary in a linear classifier. In general, this can be extended to higher dimensions as:
$$\theta_1 x_1 + \theta_2 x_2 + \dots + \theta_d x_d = 0$$
$$\theta^\top x = 0 \quad \text{or equivalently,} \quad \sum_{i=1}^d \theta_i x_i = 0$$

The set of linear classifiers is:
$$
h(x;\theta) = sign(\theta*x), \theta\in R^d
$$
This describes the set of **all linear classifiers** in d-dimensional space that pass through the origin

![[Pasted image 20250201133539.png]]

The bias term $\theta_0$ determines the position of the decision boundary relative to the origin. If $\theta_0 > 0$, the origin is in the **positive region**, meaning the decision boundary is **below** the origin. If $\theta_0 < 0$, the origin is in the **negative region**, meaning the decision boundary is **above** the origin. This shift ensures that the classifier is not forced to always pass through the origin, allowing for more flexible decision boundaries.

## Definition of linear separation
Training examples $S_n = {(x^{(i)}, y^{(i)})}$ are linearly separable if there exists a parameter vector $\hat{\theta}$ and offset parameter $\hat{\theta}$ such that $y^{(i)}(\hat{\theta} \cdot x + \hat{\theta_0}) > 0$ for all $i = 1, \dots, n$

## The perceptron algorithm
The Perceptron algorithm repeatedly adjusts the weights ($\theta$) and bias ($\theta_0$) to correct misclassified points, gradually improving the decision boundary until all points are correctly classified (if the data is linearly separable).

![[Pasted image 20250201200735.png]]
![[Pasted image 20250201200746.png]]


