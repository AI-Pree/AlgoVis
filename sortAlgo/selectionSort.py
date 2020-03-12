def compare(a, b):
    return a < b

def exch(arr,a , b):
    arr[a], arr[b] = arr[b], arr[a]

def selectionSort(arr):
    for i in range(len(arr)):
        less = i
        for j in range(i,len(arr)-1):
            if compare(arr[j+1], arr[less]):
                less = j + 1
        exch(arr,i, less)