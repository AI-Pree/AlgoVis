import numpy as np
import cv2 

#creating a grid the pixels
grid = np.zeros((300,300,3), dtype = "float32") #using hsv to match the human preceived color
print(grid.shape)

for col in range(grid.shape[1]):
    grid[:,col,:] = (col/grid.shape[1],1.0,1.0)

#converting rgb to the hsv
green = np.full_like((10,10,3),2)
print(green)
print(green.shape)
#hsv_green = cv2.cvtColor(green,cv2.COLOR_BGR2HSV)
cv2.im
#output the image file for the given grid in RGB
