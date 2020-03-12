from skimage import color
from imageio import imsave
import cv2 
import numpy as np
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap
 

'''
    Viridis color map to test the sorting algorithm
'''

img = np.zeros((50, 50, 3), dtype='float16')
viridis = cm.get_cmap("viridis", 50)
viridis_array = viridis.colors


'''
    Converting the rgba to rgb
'''
for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        img[row,col] = viridis_array[col,:-1]

imsave("viridis_rgb.png", img)

'''
    shuffling the color
'''
for col in range(img.shape[1]):
    np.random.shuffle(img[col,:,:])

imsave("viridis_shuffled.png", img)
