# AlgoVis
## Selection Sort
![](gif/selection.gif)
```python
def compare(a, b):
    return a < b

def exch(arr,a , b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def selectionSort(arr):
    for i in range(len(arr)):
        less = i
        for j in range(i,len(arr)-1):
            if compare(arr[j+1], arr[less]):
                less = j + 1
        exch(arr,i, less)
```

## Insertion Sort
![](gif/insertion.gif)
```python
def compare(a, b):
    return a < b

def exch(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp


def insertionSort():
    for i in range(len(arr)):
        j = i
        while (j > 0):
            if compare(arr[j], arr[j-1]):
                exch(arr, j, j-1)
            j -= 1
```

## Shell Sort
![](gif/shell.gif)
```python
N = len(arr)
def less(a, b):
    return a < b

def exch(arr, a, b):
    temp = arr[a]
    arr[a] = arr[b]
    arr[b] = temp

def shellSort():

    #setting h interval
    h = 1
    while(h < N/3): 
        h = h * 3 + 1 #increment sequence by 3x + 1 
        print(h)

    while (h > 0):
        for i in range(h, N):
            j = i
            while (j >= h and less(arr[j], arr[j-h])):
                exch(arr, j, j-h)
                j -= h
        h //= 3 #move to next increment
```
