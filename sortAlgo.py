from imageio import imsave
from matplotlib import cm
import numpy as np
from skimage import color

'''
    Selectionsort
'''
def selectionSort(arr):
    swaps = []
    for i in range(len(arr)):
        less = i
        for j in range(i,len(arr)-1):
            if arr[j+1] > arr[less]:
                less = j + 1
        if less != i:
            swaps.append([i,less])
            arr[i], arr[less] = arr[less], arr[i]
    return swaps


'''
    Viridis color map to test the sorting algorithm
'''
img = np.zeros((3, 3, 3), dtype='float16')
viridis = cm.get_cmap("viridis", 5)
viridis_array = viridis.colors

'''
    Converting the rgba to rgb
'''
for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        img[row,col] = viridis_array[col,:-1]

imsave("viridis_rgb.png", img) #output for the image file

rgb_hsv = color.convert_colorspace(img, "rgb", "hsv")
print(rgb_hsv)


print()
print()
print()

'''
    shuffling the color
'''

for col in range(rgb_hsv.shape[1]):
    np.random.shuffle(rgb_hsv[col,:,:])


shuffle = color.convert_colorspace(rgb_hsv,"hsv", "rgb")
imsave("viridis_shuffled.png",shuffle ) #output for the shuffled image file

test = color.convert_colorspace(shuffle, "rgb", "hsv")
print(test)

'''
    sorting values
'''
swap_nums = 0
changes = []

for i in range(img.shape[0]):
    new_change = []
    new_change = selectionSort(list(test[i,:,0]))
    if len(new_change) > swap_nums:
        swap_nums = len(new_change)
    changes.append(new_change)
print(changes)

print(test) 