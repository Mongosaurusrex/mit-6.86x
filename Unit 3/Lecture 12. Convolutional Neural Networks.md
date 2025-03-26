- Know the differences between feed-forward and Convolutional neural networks (CNNs).
    
- Implement the key parts in the CNNs, including **convolution** , **max pooling** units.
    
- Determine the dimension of each channel in different layers with a given CNNs. 

## The problem
Let say that we want to predict a image with a category, for instance mushroom to a picture of a mushrooms.

The reason why we cant use a feed-forward network is that lets say that we have this picture of a mushroom in 1000 x 1000 pixels, which gives us a $10^6$ matrix representing this picture, then we would need a hidden layer of $10^6$ to store the transformation of this picture. And in turn have a weight matrix being a $10^6 * 10^6$ matrix. Just astronomical sizes

And give that a mushroom are a little bit off center, then the classifier wouldn't find this as a mushroom.

![[Pasted image 20250313082818.png]]

If we were to slice this into smaller chunks lets say 11x11 then we would get a dimension of the weights with $11^2=121$ which is much easier to calculate and work with.
![[Pasted image 20250313083154.png]]
We loop through $11 \times 11$ regions of the image, applying the same set of weights at each step, shifting by one pixel (or more) at a time. The reason for reusing the same weights is to significantly reduce the number of parameters, making the model more efficient. This approach also ensures that important patterns, such as edges and textures, are consistently detected across the entire image.

![[Pasted image 20250313084602.png]]
