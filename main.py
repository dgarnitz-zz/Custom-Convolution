from matplotlib.image import imread
from convolution import convolution
import numpy as np

#import the image - must be PNG
# im = imread("../ImageStitch/cropped/left.png")
im =  np.array([[[1,2,3,4],[5,6,7,8],[9,8,7,6]],[[0,0,0,0],[1,1,1,1],[2,2,2,2]]])

#first convolution
convolution(2,1,im)