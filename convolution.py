import numpy as np

def convolution(dimension, stride, pixels, padding):
    #output feature maps
    feature_map=[]

    #initialize filter
    filtr = np.random.rand(dimension, dimension)
    filtr*=0.1      #scalar multiplication to reduce weights

    #variables to control the convolving                                  
    r1 = 0
    c1 = 0
    r2 = dimension
    c2= dimension

    #add padding
    if padding:
        pixels = add_padding(pixels)
        # print("Shape after padding: " + str(pixels.shape))

    #loop over the tensor and convolve
    while c2<=len(pixels):
        r1=0
        r2=dimension
        row = []

        while r2<=len(pixels[0]):
            patch = pixels[c1:c2,r1:r2]
            dot = np.tensordot(patch, filtr, axes=((0,1),(0,1)))    # patch.ravel().dot(filtr.ravel()) also works 
            dot1D = np.atleast_1d(dot)  #convert from 0D to 1D array
            row.append(dot1D[0])
            r1+=stride
            r2+=stride

        feature_map.append(row)
        c1+=stride
        c2+=stride

    return feature_map
    

# Zero PADDING
def add_padding(pixels):
    # print("Shape before padding: " + str(pixels.shape))
    pixels = np.insert(pixels,0,0,axis=0)               #along the top row
    pixels = np.insert(pixels,0,0,axis=1)               #in the first column
    pixels = np.insert(pixels,len(pixels),0,axis=0)     #along the bottom row
    pixels = np.insert(pixels,len(pixels[0]),0,axis=1)  #in the last column
    return pixels
   

#Convolutional Layer
    #NEXT STEP --> output the image
                    # Need to change VENV to work with Python3    
    #PROBLEM - weights need to persist for use in backprop
    
# Max POOLING
    #What determines the size of the pooling area? Is it that size of the convolution?

# the slicing tells it which list to go into, so [k,j,i] would be the 
# would be in the kth set [[]], in the jth brack [] of k, number i inside j 
