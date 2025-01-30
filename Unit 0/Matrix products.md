**Definition**

  Given two matrices $A$ and $B$, where:

• $A$ is an $m \times n$ matrix,

• $B$ is an $n \times p$ matrix,

  

The product $C = AB$ is defined as:

• $C$ is an $m \times p$ matrix.

• The element $c_{ij}$ of $C$ is given by:
$$c_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}$$
 where:

• $a_{ik}$ is the element of $A$ in row $i$ and column $k$,

• $b_{kj}$ is the element of $B$ in row $k$ and column $j$.

**Example**
If:
$A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}, \quad B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix},$

then $C = AB$ is:
$$C = \begin{bmatrix}

(1 \cdot 5 + 2 \cdot 7) & (1 \cdot 6 + 2 \cdot 8) \\

(3 \cdot 5 + 4 \cdot 7) & (3 \cdot 6 + 4 \cdot 8)

\end{bmatrix}

= \begin{bmatrix}

19 & 22 \\

43 & 50

\end{bmatrix}.$$
