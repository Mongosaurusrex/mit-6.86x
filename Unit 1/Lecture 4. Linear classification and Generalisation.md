- understand optimization view of learning
    
- apply optimisation algorithms such as gradient descent, stochastic gradient descent, and quadratic program

## Complexity and generalization

![[Pasted image 20250204081920.png]]
This graph illustrates the relationship between model complexity and generalization performance, particularly focusing on training and validation loss. The x-axis represents model complexity ($C$), which increases as the model becomes more flexible, while the y-axis shows the loss or error. On the left, in the underfitting region, the model is too simple to capture the data’s patterns, leading to high training and validation losses. On the right, in the overfitting region, the model is overly complex, achieving very low training loss but high validation loss as it fails to generalize to unseen data. The optimal point, marked as $C^*$, minimizes validation loss and represents the best trade-off between underfitting and overfitting.

The hinge loss function, often used in SVMs, encourages a margin of separation between classes while using regularization to penalize overly complex models. The regularization term ($\frac{\lambda}{2} \|\theta\|^2$) controls this trade-off by constraining the model’s weights. A larger $\lambda$ enforces simplicity, reducing overfitting but risking underfitting, while a smaller \lambda allows for more complexity, potentially leading to overfitting. This graph highlights the importance of selecting an appropriate regularization parameter ($\lambda$) to ensure the model generalizes well, striking a balance between fitting the training data and maintaining predictive accuracy on unseen data.

## Preface: Gradient descent
Assume $\theta \in R$. Our goal is to find $\theta$ that minimizes:
$$
J(\theta,\theta_0) = \frac{1}{n}\sum_{i=i}^n
Loss_h(y^{(i)}(\theta\cdot x^{(i)}+\theta_0))+ \frac{\lambda}{2}||\theta||^2$$through gradient descent. In other words, we will

1. Start at an arbitrary location:
$$\theta \gets \theta_{start}$$
- Update repeatedly with until $\theta$ does not change significantly:
$$\theta \gets \theta - \eta \frac{\delta J(\theta,\theta_0)}{\delta \theta}$$
## Stochastic gradient descent
![[Pasted image 20250204162937.png]]
![[Pasted image 20250204162945.png]]Stochastic Gradient Descent (SGD) is an optimization algorithm commonly used in machine learning for minimizing loss functions, including those in support vector machines (SVMs) and deep learning models. It operates by updating model parameters using small, randomly chosen subsets of the data, allowing for faster convergence compared to full-batch gradient descent. In the context of the **hinge loss function**, which is used in SVMs to enforce a margin-based separation between classes, SGD is particularly useful because it efficiently optimizes the convex but non-smooth hinge loss. The hinge loss penalizes misclassified points and correctly classified points that are too close to the decision boundary, which aligns well with the incremental updates of SGD. Unlike smooth loss functions like mean squared error, hinge loss can introduce abrupt changes in gradients, but SGD’s iterative nature helps navigate these changes effectively, making it well-suited for large-scale classification tasks.

## Quadratic Program

![[Pasted image 20250205083736.png]]

![[Pasted image 20250205083851.png]]


## Summary
- Learning problems can be formulated as optimization problems of the form: loss + regularization
- Linear, large margin classification, along with many other learning problems, can be solved with stochastic gradient descent algorithms
- Large margin linear classifier can be also obtained via solving a quadratic program (SVM)