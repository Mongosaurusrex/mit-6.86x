
- understand the problem definition and assumptions of recommender systems
    
- understand the impact of similarity measures in the K-Nearest Neighbor method
    
- understand the need to impose the low rank assumption in collaborative filtering
    
- iteratively find values of $U$ and $V$ (given $X=UV^T$) in collaborative filtering

## Introduction

- Problem definition
- KNN - algorithm
- Matrix factorization

## Problem definition

Concider a $n * m$ matrix where $n$ are users, and $m$ is a movie we can say that $y_{ai}$ is the rank of a user at spot $a$ and movie $i$.

Most of the matrix is empty, with rankings here and there... we want to fill out the matrix with ratings.

Previously we would have thought that this is a supervised/classification problem but it is not. 

The first reason is that we think that we cannot extract features from a specific movie. We just know a user and a rating.

Secondly the problem here is also estimation, we might not have enough data to predict this.

## K - Nearest neighbour Method
The goal in our movie recommender system problem is to predict the movie ranking that a user would give on a movie that (s)he has not yet seen.

Let $m$ be the number of movies and $n$ the number of users. The ranking $Y_{ai}$ of a movie $i \in \{1,\dots,m\}$ by a user $a \in \{1,\dots,n\}$ may already exist or not. Our goal is to predict $Y_{ai}$ in the case when $Y_{ai}$ does not exist.

The $K$-Nearest Neighbour method makes use of ratings by K other "similar" users when predicting $Y_{ai}$.

Let KNN (a) be the set of $K$ users "similar to" user $a$, and let $sim(a,b)$ be a **similarity measure** between users $a$ and $b \in KNN(a)$. The $K$-nearest Neighbour method predicts a ranking $Y_{ai}$ to be:
$$
\hat Y_{ai} = \frac{\sum_{b\in KNN(a)} sim(a,b)Y_{bi}}{\sum_{b\in KNN(a)} sim(a,b)}
$$
The similarity measure $sim(a,b)$ could be any distance function between the feature vectors $x_a$ and $x_b$ of users $a$ and $b$, e.g. the euclidean distance $||x_a - x_b||$ and the cosine similarity $cos\theta = \frac{x_a \cdot x_b}{||x_a||||x_b||}$ . We will use these similarity measures again in Unit 4.

A drawback of this method is that the success of the $K$-Nearest Neighbour method depends heavily on the choice of the similarity measure.

## Collaborative Filtering: The Naive Approach

The Naive approach bases on the fact that we try to approach the the problem from a linear regression perspective such that there is $J(X)$ that satisfies:
$$
J(X)=\sum_{a,i\in D}\frac{(Y_{ai}-X_{ai})^2}{2} + \frac{\lambda}{2}\sum_{(a,i)}X^2_{ai}
$$
Which in turn maximises by:
$$
\hat X_{ai}=\frac{Y_{ai}}{1+\lambda}, (a,i) \in D
$$
$$
\hat X_{ai}=0, (a,i)\not\in
D$$

## Collaborative Filtering: Matrix Factorization
