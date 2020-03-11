arr = [1,4,3,6,7,3,4,6,12,3,3,43,65]

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
selectionSort(arr)
print(arr)