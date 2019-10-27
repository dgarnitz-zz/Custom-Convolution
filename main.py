from matplotlib.image import imread
from convolution import convolution
from max_pool import max_pool
import numpy as np
import scipy.misc as smp

#get configurations from the user - filter size
dimension = 0
while True:
    print("Please enter the length of the convolutional filter in range 0-7. \nIt will be in a square filter of the formform 'LxL'.")
    dimension = int(input())
    if dimension>=0 and dimension<=7:
        break

#get configurations from the user - stride
stride = 0
while True:
    print("Please enter the length of the stride in range 0-5. \nIt will be both horizontal and vertical stride.")
    stride = int(input())
    if stride>=0 and stride<=5:
        break

#get configurations from the user - zero padding
padding = ""
while True:
    print("Do you want zero-padding? \nEnter 'yes' or 'no'.")
    padding = input()
    if padding=="yes" or padding=="no":
        break

pad = True if padding=='yes' else False

#import the image - must be PNG - loads pixels in 0-1 scale (pixel value divided by 255)
img = imread("../ImageStitch/cropped/left.png")
# im =  np.array([[[1,2,3,4],[5,6,7,8],[9,8,7,6]],[[0,0,0,0],[1,1,1,1],[2,2,2,2]]])

#reshape the array to make it easier to convolve over
tensor = np.reshape(img, (len(img[0][0]),len(img[0]),len(img)))

#store the feature maps output by the convolution
features = []

# first convolution
for i in range(len(tensor)):
    features.append(convolution(dimension,stride,tensor[i],pad))

features = np.asarray(features)
print(features.shape)

#store the output of the pooling
pooled_features = []

# Max Pooling
for i in range(len(features)):
    pooled_features.append(max_pool(features[i],dimension))

pooled_features = np.asarray(pooled_features)
print(pooled_features.shape)

# #reshape the array to it can be output
# features = np.reshape(features,(len(features[0][0]),len(features[0]),len(features)))
# print(features.shape)

# #print the altered image
# image = smp.toimage( features )
# image.show()
