import numpy as np

def convolution(dimension, stride, pixels):
    #initialize filter
    filter = np.random.rand(dimension, dimension)

    #grab each channel matrix
    r1 = 0
    c1 = 0
    r2 = dimension
    c2= dimension
                                    # eventually you will want to get rid of this - convolution 
    for i in range(len(pixels)):    # should only be on ONE channel to create ONE feature map
        r1 = 0
        c1 = 0
        r2 = dimension
        c2= dimension

        while c2<=len(pixels[0]):
            patch = pixels[i,c1:c2,r1:r2]
            dot = np.dot(patch, filter)     
            print(dot)
            c1+=stride
            c2+=stride


    print(len(pixels[0]))
    # print(filter.shape==patch.shape)

#you need first the # of channels, iterate over that    

# the slicing tells it which list to go into, so [k,j,i] would be the 
# would be in the kth set [[]], in the jth brack [] of k, number i inside j 
