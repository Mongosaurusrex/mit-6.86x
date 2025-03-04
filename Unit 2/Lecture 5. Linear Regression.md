- write the training error as least squares criterion for linear regression
    
- use stochastic gradient descent for fitting linear regression models
    
- solve closed-form linear regression solution
    
- identify regularization term and how it changes the solution, generalization'


## Classification vs Linear regression

By definition we want to in a linear classificator predict an observed value as a real number $y \in R$ instead of $y \in \{-1,1\}$ 

The predictor $f$ is a linear function of the feature vectors. i.e. 
$$
f(x) = \sum_{i=1}^d\theta_ix_i+\theta_0
$$
where $d$ is a integer of known instances of feature vectors

## Empirical Risk

The empirical risk is just another way of saying the error of our regression.
$$
R(\theta) = \frac{1}{n}\sum_{t=1}\frac{(y^t-\theta x^t)^2}{2}
$$
The way of handling the empirical risk of our model is by using the mean squared error. Where we say that a small deviation is ok, but the bigger the deviation is then we penalize it more.

There are two distinct issues that can happen in basically any machinelearning situation, **structural issues** and **estimation issues**

**Structural Issues (Bias / Model Complexity)**
• **Cause**: Model class is too simple or too complex.

• **Effect**: Leads to **high bias** (underfitting) or **overfitting**.

• **Example**: Trying to fit a **linear model** to data that follows a quadratic relationship.

**Estimation Issues (Variance / Data-Related Problems)**
• **Cause**: Limited training data or noisy data.

• **Effect**: Leads to **high variance** in parameter estimates.

• **Example**: Fitting a **high-degree polynomial** to a small dataset, leading to wildly different results based on the training points.

## Gradient based approach
$$
J(\theta) = \frac{1}{2}(y^{(t)}-\theta x^{(t)})^2
$$
$$
\nabla_\theta J(\theta) = \nabla_\theta\frac{1}{2}(y^{(t)}-\theta x^{(t)})^2
$$
$$
=\frac{1}{2}*\nabla_\theta[g(u)]
$$$$
g(u)=u^2, u=y^{(t)}-\theta x^{(t)}
$$$$
= \frac{1}{2}*2u\nabla_\theta u
$$$$
= u * \nabla_\theta (y^{(t)}-\theta x^{(t)})
$$$$
= (y^{(t)}-\theta x^{(t)})(-x^{(t)})
$$$$
= -(y^{(t)}-\theta x^{(t)})x^{(t)}
$$
**Gradient decent update rule:**
$$
\theta \leftarrow \theta + \alpha (y^{(t)} - \theta x^{(t)}) x^{(t)}
$$
## Closed form solution
$$
\nabla R_n(\theta) = A\theta - b = 0
$$
where:
$$A = \frac{1}{n} \sum_{t=1}^{n} x^{(t)} (x^{(t)})^T = \frac{1}{n} X^T X$$$$b = \frac{1}{n} \sum_{t=1}^{n} y^{(t)} x^{(t)} = \frac{1}{n} X^T y$$
Gives:
  $$\theta = (X^T X)^{-1} X^T y$$

**Example**:
Given:
$$X =

\begin{bmatrix}

1 & 2 \\

2 & 3 \\

3 & 5

\end{bmatrix}
$$$$

y =

\begin{bmatrix}

2 \\

3 \\

4

\end{bmatrix}
$$We compute:
$$A = X^T X =

\begin{bmatrix}

1 & 2 & 3 \\

2 & 3 & 5

\end{bmatrix}

\begin{bmatrix}

1 & 2 \\

2 & 3 \\

3 & 5

\end{bmatrix}$$
$$b = X^T y =

\begin{bmatrix}

1 & 2 & 3 \\

2 & 3 & 5

\end{bmatrix}

\begin{bmatrix}

2 \\

3 \\

4

\end{bmatrix}$$

Solving  $\theta = A^{-1} b$, we get:

$$\theta =

\begin{bmatrix}

0.3333 \\

0.6667

\end{bmatrix}$$

Thus, our regression equation is:
$$\hat{y} = 0.3333 + 0.6667 x$$

## Ridge regression

The regression over time is described by:
$$
J_{n,\lambda}(\theta,\theta_0)=\frac{1}{n}\sum_{t=1}^n\frac{(y^{(t)}-\theta \cdot x^{(t)} - \theta_0)^2}{2} + \frac{\lambda}{2}||\theta||
$$

## Closing thoughts
The ridge regression formulae balances two components in linear regression, one is the empirical risk where we try to minimize our data loss to our data. The second part is making the theta small. Why would you want to push to make mistakes given that the empirical risk is trying to make the loss small? That is because we want to generalize by not overfitting on the data and make it perform better in a non training data