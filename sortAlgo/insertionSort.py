arr = [1,23,4,2,332,43,23,4,54,23,5,4]

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

insertionSort()
print(arr)