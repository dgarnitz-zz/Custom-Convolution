import numpy as np

def max_pool(features, dimension, stride):
    #output feature maps
    feature_map=[]

    #variables to control the pooling                                  
    r1 = 0
    c1 = 0
    r2 = dimension
    c2= dimension

    #loop over the tensor and convolve
    while c2<=len(features):
        r1=0
        r2=dimension
        row = []

        while r2<=len(features[0]):
            patch = features[c1:c2,r1:r2]
            pooled_value = pool(patch)
            row.append(pooled_value)
            r1+=stride
            r2+=stride

        feature_map.append(row)
        c1+=stride
        c2+=stride

    return feature_map

def pool(patch):
    max = -1
    for val in patch.flatten(): #this could also be done with np.amax after flattening
        if val > max:
            max = val
    return val