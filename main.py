def DNF(a, s):
    low = 0
    high = s - 1
    mid = 0
    while mid <= high and low <= high:
        if a[mid] == 0:
            a[low], a[mid] = a[mid], a[low]
            low = low + 1
            mid = mid + 1
        else:
            if a[mid] == 1:
                mid = mid + 1
            else:
                a[mid], a[high] = a[high], a[mid]
                high = high - 1
    return a


def printArray(a):
    for k in a:
        print(k, end=' ')


arr = [ 1, 1, 2, 0, 2, 1]
s = len(arr)
arr = DNF(arr, s)
printArray(arr)
