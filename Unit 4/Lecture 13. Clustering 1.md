- Understand the definition of **clustering**
- Understand **clustering cost** with different similarity measures
- Understand the **K-means** algorithm

# Introduction to clustering
A typical clustering (unsupervised learning) can be distinguished from supervised learning by the the data being different in the label aspect, we do not know the label of a datapoint.

$$ 
Classification: S_n=\{(x^{(i)},y^{(i)}|i=1,\dots,n\}
$$
$$
Clustering: S_n=\{(x^{(i)}|i=1,\dots,n)\}
$$
When we look into the clustering as a problem we will try to look into the similarities of the points and calculate it somehow.

## Clustering definition
$$
Clustering: S_n=\{(x^{(i)}|i=1,\dots,n)\}, K
$$
$$
Partition: C_1 \cup C_2 \cup \dots\cup C_K = \{1,2,\dots,n\}
$$
$$
And: C_j \cap C_i = ∅, i\neq j
$$
## Similarity Measures-cost functions
We need to have some kind of a measurement of knowing which combination of clustering is better than another.
$$
cost(C_1,\dots,C_K) = \sum_{j=1}^Kcost(C_j)
$$
$$
cost(C,z)=\sum_{i\in C}
dist(x^{(i)},z)
$$

Given the idea that we must try to compute the best clustering permutation given $K$ we can define these two functions:
$$
\sum_{j=1}^K\sum_{i\in C}
dist(x^{(i)},z)
$$
Where the alternatives for $dist$ are:
$$
cos(x^{(i)},x^{(j)})=\frac{x^{(i)}\cdot x^{(j)}}{||x^{(i)}||\cdot||x^{(i)}||}
$$
$$
dist(x^{(i)},x^{(j)})=||x^{(i)}-x^{(j)}||^2
$$
## K-means clustering algorithm
- The value of $z_j$ is only affected by the points in the cluster j, the points $\{x_i:i\in C_j\}$ and not the points in the other clusters: the points $\{x_i:i\not\in C_j\}$ .

- $z_j$ is the centroid of the $j$th cluster $C_j$ or the center of mass.

- $C_1,\dots,C_k$found by the algo is always a partition of the set of points

For cluster j minimise 
$$
\sum_{i\in C_j}||x_i z_j||
$^2
$$
Taking the derivative with respect to $z_j$ : 
$$
\frac{\partial}{\partial z_j} \sum_{i \in C_j} \| x_i - z_j \|^2$$
$$= \sum_{i \in C_j} -2(x_i - z_j)$$
Equal to zero and solve for $z_j$:
$$\sum_{i \in C_j} -2(x_i - z_j) = 0$$
$$z_j = {\sum_{i \in C_j} x_i \over | C_j | }$$
$z_j$ is the centroid of the cluster.

Euclidean distance:

- derivative is easy (compare to other distance functions)

#### Convergence

We are sure that algo will converge to a local minimun

Because

- Cost funciton is not 0
- At every step, Stay the same or decrease
- Partition is finate

#### Impact of Initialization

Order of magnitude

Note:

- If K=1, the initialization doesn't influence the result, because the cluster assigment (in step 2.1) will asign all points to the unique cluster.

K-Means

- Advantages:
    - It is relatively efficient with time complexity O(nkt). Scale well to large datasets.
- Drawbacks:
    - Very sensistive to initialization (10'20)
    - It requires to specify manually the number of clusters (k) in advance.
    - It can not handle noisy data and outliers.
    - Does not scale well with increasing number of dimensions (the curse of dimentionality)
    - It is not suitable to identify clusters with non-convex shapes.