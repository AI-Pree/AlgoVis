from imageio import imsave
from matplotlib import cm
import numpy as np
from skimage import color

'''
    Selection sort
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
    insertion sort
'''
def insertionSort(arr):
    swaps = []
    for i in range(len(arr)):
        key = arr[i]
        j = i
        while (j > 0 and key > arr[j-1]):
            swaps.append([j,j-1])
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return swaps

'''
    shell short
'''
def shellSort(arr):
    N = len(arr)
    swaps = []
    #setting h interval
    h = 1
    while(h < N/3): 
        h = h * 3 + 1 #increment sequence by 3x + 1 
        print(h)

    while (h > 0):
        for i in range(h, N):
            j = i
            while (j >= h and arr[j]< arr[j-h]):
                swaps.append([j,j-h])
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j -= h
        h //= 3 #move to next increment
    return arr, swaps

'''
    bubble short
'''
def bubblesort(arr):
    swaps = []
    N = len(arr)
    for i in range(N):
        for x in range(0,N-i-1):
            if arr[x] < arr[x+1]:
                swaps.append([x,x+1])
                arr[x], arr[x+1] = arr[x+1], arr[x]
    return swaps

'''
    Viridis color map to test the sorting algorithm
'''
img = np.zeros((200, 200, 3), dtype='float16')
viridis = cm.get_cmap("viridis", 200)
viridis_array = viridis.colors

'''
    Converting the rgba to rgb
'''
for row in range(img.shape[0]):
    for col in range(img.shape[1]):
        img[row,col] = viridis_array[col,:-1]

imsave("viridis_rgb.png", img) #output for the image file

rgb_hsv = color.convert_colorspace(img, "rgb", "hsv")

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

for i in range(test.shape[0]):
    new_change = []
    new_change = insertionSort(list(test[i,:,0]))
    if len(new_change) > swap_nums:
        swap_nums = len(new_change)
    changes.append(new_change)


'''
    visulization for the algorithm
'''

curr_swaps = 0

def  swap_pixels(row, value):
    tmp = test[row,value[0],:].copy()
    test[row,value[0],:] = test[row,value[1],:]
    test[row,value[1],:] = tmp

print(swap_nums)
img_trans = swap_nums // 100
img_frame = 0

while curr_swaps < swap_nums:
    for i in range(test.shape[0]):
        if curr_swaps < len(changes[i]) - 1:
            swap_pixels(i, changes[i][curr_swaps])
    
    if  curr_swaps % img_trans == 0:
        print(img_frame)
        imsave('%s/%05d.png'%("sort",img_frame), color.convert_colorspace(test, "hsv", "rgb"))
        img_frame += 1
    
    curr_swaps += 1
