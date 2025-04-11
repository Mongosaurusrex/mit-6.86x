- Understand the **limitations** of the **K-Means** algorithm
    
- Understand how **K-Medoids** algorithm is different from the K-Means algorithm
    
- Understand the **computational complexity** of the K-Means and the K-Medoids algorithms
    
- Understand the importance of choosing the right number of clusters
    
- Understand elements that can be supervised in unsupervised learning

## Limitations of the K Means Algoritm

Reminder: Based on $Cost(C_1, \dots, C_k, z_1, \dots, z_k)$
$$\sum_{j=1}^k \sum_{i \in C_j} \| x - z \|^2$$
(1) Randomly initialize  
(2) Iterate until no change in cost  
. (2a) group the points together with the closest center  
. (2b) re-calculate the centers

### Limitation 1
z's are actually not guaranteed to be the members of the original set of points x.
It's an issue for visualisation.
Its not always guaranteed that the $k$ representatives $z_1,\dots,z_k$are in the set of points $\{x_1, \dots, x_n\}$.

### Limitation 2 
The algorithm can't work with other distances, because the optimization which calculate the derivative only work with Euclidean distance

Notes:
![kmeans](https://raw.githubusercontent.com/sbeignez/MITx-6.86x-Machine-Learning/9493df645c03310d3c54c873d41ec3c1f51313ff/26.%20Unit%204.%20Lecture%2014.%20Clustering%202/img/A-schematic-diagram-of-convolution-and-max-pooling-layer-In-the-convolution-layer-a.svg)
- Left plot: No generalization, resulting in a non-intuitive cluster boundary.
- Center plot: Allow different cluster widths, resulting in more intuitive clusters of different sizes.
- Right plot: Besides different cluster widths, allow different widths per dimension, resulting in elliptical instead of spherical clusters, improving the result.

## Introduction to K-medoids algorithm
The K-Medoids algorithm is a variation of the K-Means algorithm that addresses some of the K-Means algorithm's limitations.

(1) INITIALIZATION: Randomly select the $\{ z_1,..., z_k\}$ **in** $\{ x_1,..., x_n \}$

(2) LOOP: Iterate (until..)

(2.1) ASIGN: Given, assign each $x_i$ to the closest $z_i$, so that the cost function is minimized
$$Cost(..) = \sum_i min_{j=1,...,k} dist(x_i, z_j)$$
(2.2) Given $C_j$ find the best representative $z_j$ in $C_j$ such that:
$$\sum_{x \in Cj} dist()$$
is minimal.

Note:

- The Medoid algo differs:
    - step (1), initialisation is limited to x's (vs. totally random)
    - step (2.1), same.
    - step (2.2) find the cost-minizing representative for ANY given distance measure (vs. Euclidean only)

## Computational complexity of K-means and K-Medoids

Calculate the complexity:
Be:
- number of clusters k
- number of points n
- vector dimensionality d

| Step  | K Mean   | K Medoids  |
| ----- | -------- | ---------- |
| 1     | $O(k)$   | $O(k)$     |
| 2     | ..       | ..         |
| 2.1   | $O(nkd)$ | O(nkd)     |
| 2.2   | $O(nkd)$ | $O(n^2kd)$ |
| Total | $O(nkd)$ | $O(n^2kd)$ |
## Determining the number of clusters K

Choosing K:
$1<K<N$
1: All points are in one cluster (cost is the highest)
N: All points are its own representative (cost = 0)

Case:
Supervised learning with very few points with labels and/or many points un labeled. Can use clustering as pre-processing. And better find the decision boundary. 

## Final thoughts on the unsupervised learning

Not totally unsupervised: "Supervised Elements of Unsupervised Learning" are the paramters that we need to provide to the machine

- K, the number of clusters
- The similarity / cost measure