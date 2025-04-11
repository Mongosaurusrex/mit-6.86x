- Understand what **Generative Models** are and how they work
    
- Understand estimation and prediction phases of generative models
    
- Derive a relation connecting generative and discriminative models
    
- Derive **Maximum Likelihood Estimates (MLE)** for multinomial and Gaussian generative models

## Generative vs. Discriminative Models

**Generative models** work by explicitly modelling the probability distribution of each of the individual classes in the training data. For instance, Gaussian generative models fit a Gaussian probability distribution to the training data in order to estimate the probability of a new data point belonging to different classes during prediction.

**Discriminative models** learn explicit decision boundary between classes. For instance, SVM classifier which is a discriminative model learns its decision boundary by maximizing the distance between training data points and a learned decision boundary.

## Simple multinomial generative model

Ex: documents of text  
Model will generate a document, by picking a word at a time vs. vector of fixed length

Let's:

- M: a multinomial model (to generate text in documents)
- W: a vocabulary
- $p(w|\theta)$ with $\theta$ the parameter of the model, or also represented as $\theta_w$: capture the likelihood of selecting a word, given all possibilities.

To have a valid probability distribution, the constraints are:
- $\theta_w \geq 0$ (each probability is greater than 0, no negatives)
- $\sum_{w\in w}\theta_w = 1$ (sum of all probabilities is equal to 1)

#### Notes:

Why is this model called "multinomial" generative model?

- because of the number of outcomes. If there are two outcomes it is binomial. In the context of the example, there are many words (more than two), so it's called multinomial.
## Likelihood function

How do we calculate the probability $p$ to generate document $D$:
1. It's the product of the probabilities to pick each n words of $D$;
   $$p(D | \theta) = \prod_{i=1}^n \theta_{w_i}$$
2. Or the product of probability of each word to the power of its occurrence;
   $$p(D | \theta) = \prod_{w \in W} \theta_{w}^{count(w)}$$
## Maximum Likelihood estimate (MLE)

How to use the training data to find the best parameter that fit data?

Find $\theta$ such as:
$$max_{\theta} \ p(D|\theta)$$
$$max_{\theta} \prod_{w \in W} \theta_w^{count(w)}$$

It's equivalent to (and easier than) maximise the log of the product (which becomes a sum):
$$max_{\theta} \sum_{w \in W} log(\theta_w^{count(w)})$$
$$max_{\theta} \sum_{w \in W} count(w) * log(\theta_w)$$
Note:

- Log, usually refers to the logarithm of base 10, or common logarithm
- Ln, the natural logarithm, is the log base e. $lnx = log_ex$ 

### Case n = 2
$$\theta = { count(0) \over (count(0) + count(1)) }$$

## MLE for Multinomial Distribution

### Case n > 2
Vocabulary on any length
$$\theta_{w_x} = { count(w_x) \over \sum_{w \in W} (count(w)) }$$
with $\sum count(w) = n$ the size of the vocabulary W
This technique is also applicable to a collection of documents $D_1,\dots ,D_n$ by concatenating all the documents.
The assumption is that each word is generated independently

## Predictions

$$\log \frac{P(D \mid \theta^+)}{P(D \mid \theta^-)} =

\begin{cases}

\geq 0, + \\

< 0, -

\end{cases}$$
Which eventually will be made into a linear classifier
$$\sum_{w \in W} \left( \text{count}(w) \cdot \theta'_w \right) \geq 0 \quad \text{where } \theta'_w = \log \frac{\theta^+_w}{\theta^-_w}$$

## Prior, Posterior and Likelihood

Bayesian Rule:
$$p(A|B) = p(B|A) *P(A) / P(B)$$
In our predictory case:
$$P( {y=+} | D ) = P( D | \theta+) * P(y=+) / P(D)$$

In this equation:
- The prior distribution is $P(y=+)$
- the posterior distribution is $P(y=+|D)$

### Note: Probability vs. Likelihood ?

- Probability is used to finding the chance of occurrence of a particular situation. Probability attaches to possible results.
- whereas Likelihood is used to generally maximizing the chances of a particular situation to occur. likelihood attaches to hypotheses.
- [https://www.youtube.com/watch?v=pYxNSUDSFH4](https://www.youtube.com/watch?v=pYxNSUDSFH4)
    - pr( condition or data | given a distribution )
    - L ( a distribution | given an observation )

## Gaussian Generative models
Vectors $x \in R^d$

The distribution is characterised by 2 parameters:

- $\mu$, the center (or mean)
- $\sigma^2$, the dispersion of the cloud of points, the square of the average distance from mu
Assumption: The points can be models as clouds with center and dispersion. Not all data set are this way? Analyst decide which class of models is appropriate.

$$ P(X | \mu, \sigma^2 ) = {1 \over (2 \pi \sigma^2)^{d/2}} * e^{-1/{2 \sigma^2} ||X - \mu||^2}$$


