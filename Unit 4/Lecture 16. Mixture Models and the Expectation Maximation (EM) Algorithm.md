- Review **Maximum Likelihood Estimation** (MLE) of mean and variance in Gaussian statistical model
    
- Define **Mixture Models**
    
- Understand and derive ML estimates of mean and variance of Gaussians in an **Observed Gaussian Mixture Model**
    
- Understand **Expectation Maximization (EM) algorithm** to estimate mean and variance of Gaussians in an **Unobserved Gaussian Mixture Model**

## Recap
So far, in clustering we have assumed that the data has no probabilistic generative model attached to it, and we have used various iterative algorithms based on similarity measures to come up with a way to group similar data points into clusters.

Multinomials In case of language: Such as mono, bi-nomials, .. Given:

- W, the vocabulary, the set of all words
- $\theta$ the likelihood
- Sum is 1 for all $\theta_w$
- All $\theta_w \geq 0$

Then:
- The likelihood to generate a document D with words $w_1,\dots,w_n$
$$P(D | \theta) = \prod_{w\in W}\theta^{n}_w$$
For Gaussians:
- $\mu$ a center
- $\sigma^2$ a variance
- d as a dimension of the vector

**MLE** 
$$\hat\mu=\frac{1}{n}\sum_{i=1}^{n}x^{(n)}$$
$$\hat\sigma=\frac{1}{nd}\sum_{i=1}^{n}||x^{(i)}-\mu||^2$$

## Introduction to Mixture Models

Additions to previous models:
- Mixture components: More that 1 one component which each of them have gaussian parameters
- Mixture of weights

for K clusters:
$$
p(x|\theta) = \sum_j^K p_j * N(x, \mu_1, ..., \sigma^2_1, ...)
$$

Soft clustering, the model can calculate the probabilities that x belongs to each gaussian
$$
p(x|\theta) = \sum_j^K p_j * N(x, \mu_1, ..., \sigma^2_1, ...)
$$

## Estimating the parameter in the observed case

Objective: How to solve and find the parameters (the mixture weights $p_j$ the $\mu$ and $\sigma^2$)?

Simplest case, also known as the "observed case". Where we know where each point belong

Helpful function to determine if point i is in component j:
$$
\partial(j | i ) =
\begin{cases}

1, if\ x^{(i)}\in j \\

0, otherwise

\end{cases}$$
Then:
$$
\hat n_j = \sum_i^n \partial(j|i)
$$
$$
\hat p_j = \frac{\hat n_j}{n}
$$
$$
\hat\mu=\frac{1}{\hat n_j}\sum_{i=1}^{n}\partial(j | i )x^{(n)}
$$
$$
\hat\sigma^2_j = { 1 \over \hat n_j d} * \sum_{i=1}^{n}\partial(j | i )||x^{(i)}-\mu||^2$$
## Estimating the parameters in the unobserved case: EM Algorithm

#### E-step
