## Machine learning is everywhere

Search queries, content recommendation, image/scene analysis, machine translations, dialogue systems, game playing etc.

### What is it?
As a discipline it aims to design, understand and apply computer programs that learn from experience, for the purpose of modeling, prediction or control.

### Prediction problems:
Future events:
- collision avoidance
- monitoring
- medical risks 
- etc
About properties we don't know yet:
- Movie recommendation?
- Soluble in water?
- what is the image about?
- What is this sentence in Spanish

## Supervised learning

It is easier to express tasks in terms of examples of what you want (rather than how to solve them).
E.g Image classification 
![[Pasted image 20250130192847.png]]

Rather than specify the task directly (hard), we automate the process of finding one based on examples.

What we want to do is we hypothesize a set of possible mappings, an image and a category.

Eg. Translations
![[Pasted image 20250130193239.png]]
Same approach is used in machine translations, we create a mapping of a English and its Spanish translation.

## A concrete example: Movie recommender problem
I have a set of movies that I've seen, I would like to get recommendations of whether I would like to see tens of thousands of other movies.

My data (movies and if I liked it):
- Fury: -1
- Gone girl: -1
- Interstellar: +1
- Minions: +1

I have now 4 annotated examples of movies I liked and I need to get a recommendation of what I will like out of thousands of other unseen movies.
Computers understand my rating very well but they dont understand the movie out of itself so we will have to create a feature vector out of each movie, for instance:

$$
x^{(1)}=[1, 0 ,0 ,1,1,...,0]^T
$$
Where $x$ is the vector $(1)$ superscript denotes the identity of the movie in the set of examples that we have.

We will construct the feature vector by asking questions about those movies, for example if it is an action movie 0 or 1. Is it a comedy 0 or 1 etc. Add many of these questions and associate this to a vector that represents the movie.

Given this with our movie list:
- Fury: -1 ; $x^{(1)}$
- Gone girl: -1 ; $x^{(2)}$
- Interstellar: +1 ; $x^{(3)}$
- Minions: +1 ; $x^{(4)}$
Which can be called a training set, which I have classified given a vector to a certain rating.
And the vast majority of other data that I have yet to experience/rate I call the test data, data that I wish to predict a rating on given the classification.

### Geometric representation
![[Pasted image 20250130195335.png]]

We have all movies representations as points $(x^{(1)}, y^{(1)})$ in space $x^{(1)}$ etc, with their associated labels $y^{(1)} = -1$ for instance.
The training set is denoted by $S_n$, with $n=4$

$$
S_n, (x^{(i)},y^{(i)}), i=1,...,n
$$
![[Pasted image 20250130200103.png]]
The task I have is to predict the label for each of the unknown point in space for the points in the test set. What we need is a classifier $h$ that maps:
$$
h:X \to \{-1,1\}
$$
$$
h(x) = 1
$$
### Linear classifiers
![[Pasted image 20250130200556.png]]

I linear classifier divides the space into two halves, as example in the blue part we classify everything as +1. This isn't really a good classifier because it mislabels things.

We need to evaluate the classifier, we define a training error $E_n(h)$ .
In this case we will count the error $E_n$ as:
$$
E_n(h)= \frac{1}{n}\sum_{i=1}^{n}[h(x^{(i)}) \ne y^{(i)}]
$$
In this example $E_n(h) = 1/2$

![[Pasted image 20250130201252.png]]
Better! $E_n(h) = 0$

![[Pasted image 20250130201344.png]]
Also good! $E_n(h) = 0$

![[Pasted image 20250130201509.png]]
Extreme example, but $E_n(h) = 0$, overfitting example. "An example of generalisation", how well does a classifier explain and predict a general situation, and in the last example probably not so good

## Classification vs Regression
![[Pasted image 20250131124320.png]]
Multi-way classification: Is a classifier that categorises more than two  labels
Regression: An outcome that gives a real number rather than a category
Structured prediction: More of an object, picture -> describing scentence

![[Pasted image 20250131124618.png]]

## Summary:
- Posing supervised machine learning problems
- Supervised classification
- The role of training/test sets
- A classifier
- A set of classifiers
- Errors, generalization
