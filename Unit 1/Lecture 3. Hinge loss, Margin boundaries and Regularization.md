- understand the need for maximizing the margin
    
- pose linear classification as an optimization problem
    
- understand hinge loss, margin boundaries and regularization

![[Pasted image 20250202191910.png]]
When deciding for a linear classifier we would rather like to use the one that has a lot of "room" around the things that it is trying to predict, and lets try to motivate it mathematically
![[Pasted image 20250202192356.png]]
Think of the margin as a safety buffer between the two classes. The wider the margin, the better the classifier can separate them without relying too much on specific training points. If we push the margin. We look at this because of us not being too close to a training point an therefore handle overfitting hopefully...

![[Pasted image 20250203093749.png]]
**Summary of the Margin in Linear Classification**

1. **Key Concept:**
	• The margin measures the **perpendicular distance** between a data point  $x_i$ and the decision boundary  $\theta \cdot x + \theta_0 = 0$ , normalized by  $\|\theta\|$ .

2. **Expression for the Margin:**
$$\frac{y_i (\theta \cdot x_i + \theta_0)}{\|\theta\|}$$
$y_i$ ($\theta \cdot x_i + \theta_0$) : Determines if the point is correctly classified.

	 Positive: Correctly classified.

	• Negative: Misclassified.

Dividing by  $\|\theta\|$ : Normalizes the margin, making it scale-independent and geometrically meaningful.

3. **Margin Interpretation:**

$\geq 1$: Correctly classified and **outside the margin** (safe zone).

$0 < \text{value} < 1$ : Correctly classified but **inside the margin** (less confident).

• < 0 : Misclassified (wrong side of the boundary).

4. **Goal in SVMs:**

• Maximize the margin $\frac{1}{\|\theta\|}$ , which separates classes with the greatest possible distance, improving generalization.

![[Pasted image 20250203095636.png]]
1. **Hinge Loss:** Penalizes points inside the margin or misclassified.

2. **Regularization:** Encourages a wide margin by minimizing  $\|\theta\|^2$ .

3. **Objective Function:** Combines these two goals to find the best trade-off using  $\lambda$ .
	1. High $\lambda$ means more emphasis on the regulation
	2. Low $\lambda$ more emphasis on the loss

![[Pasted image 20250203101229.png]]