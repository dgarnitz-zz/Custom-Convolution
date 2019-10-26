import numpy as np

def convolution(dimension, stride, pixels):
    #output feature maps
    features = []

    #initialize filter
    filtr = np.random.rand(dimension, dimension)

    #variables for convolving
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
        feature_map=[]

        while c2<=len(pixels[0]):
            r1=0
            r2=dimension
            row = []

            while r2<=len(pixels[0][0]):
                patch = pixels[i,c1:c2,r1:r2]
                dot = np.tensordot(patch, filtr, axes=((0,1),(0,1)))    # patch.ravel().dot(filtr.ravel()) also works 
                dot1D = np.atleast_1d(dot)  #convert from 0D to 1D array
                row.append(dot1D[0])
                r1+=stride
                r2+=stride

            feature_map.append(row)
            c1+=stride
            c2+=stride

        features.append(feature_map)

    features = np.asarray(features)
    print(features)
    # print(filter.shape==patch.shape)

#Convolutional Layer
    #NEXT STEP --> append each tensordot to an output list [] feature map 
    #PROBLEM - weights need to persist for use in backprop
    
# Max POOLING
    #What determines the size of the pooling area? Is it that size of the convolution?

# Zero PADDING   

# the slicing tells it which list to go into, so [k,j,i] would be the 
# would be in the kth set [[]], in the jth brack [] of k, number i inside j 
