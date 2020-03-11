arr = [1,3,4,5,6,7,8,23,4,5,6,342,54,65]
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
shellSort()
print(arr)
