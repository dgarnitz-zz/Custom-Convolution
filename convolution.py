import numpy as np

def convolution(dimension, stride, pixels):
    #initialize filter
    filter = np.random.rand(dimension, dimension)

    #grab each channel matrix
    r1 = 0
    c1 = 0
    r2 = dimension
    c2= dimension
    patch = pixels[0,c1:c2,r1:r2]
    dot = np.dot(patch, filter)     #can replace this with a manual implementation later
    print(dot)
    # print(filter.shape==patch.shape)

#you need first the # of channels, iterate over that    

# the slicing tells it which list to go into, so [k,j,i] would be the 
# would be in the kth set [[]], in the jth brack [] of k, number i inside j 
