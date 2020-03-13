# AlgoVis
## Selection Sort
![](gif/selection.gif)
```python

def selectionSort(arr):
    for i in range(len(arr)):
        less = i
        for j in range(i,len(arr)-1):
            if arr[j+1] > arr[less]:
                less = j + 1
        if less != i:
             arr[i], arr[less] = arr[less], arr[i]
```

## Insertion Sort
![](gif/insertion.gif)
```python
def insertionSort(arr):
    for i in range(len(arr)):
        j = i
        while (j > 0):
            if arr[j] > arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
```

## Shell Sort
![](gif/shell.gif)
```python
def shellSort(arr):
    N = len(arr)
    #setting h interval
    h = 1
    while(h < N/3): 
        h = h * 3 + 1 #increment sequence by 3x + 1 

    while (h > 0):
        for i in range(h, N):
            j = i
            while (j >= h and arr[j] < arr[j-h]):
                arr[j], arr[j-h] = arr[j-h], arr[j]
                j -= h
        h //= 3 #move to next increment
```
