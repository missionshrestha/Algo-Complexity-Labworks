from math import floor
from sys import maxsize


def merge_sort(arr, lb, rb):
    if (lb < rb):
        mid = floor((lb+rb)/2)
        merge_sort(arr, lb, mid)
        merge_sort(arr, mid+1, rb)
        merge(arr, lb, mid, rb)
    return arr


def merge(arr, lb, mid, rb):
    n1 = mid-lb+1
    n2 = rb-mid
    # left_arr = [n1]
    # right_arr = [n2]
    left_arr = [0] * (n1+1)
    right_arr = [0] * (n2+1)

    
    for i in range(0, n1):
        left_arr[i] = arr[lb+i]

    for j in range(0, n2):
        right_arr[j] = arr[mid+j+1]

    left_arr[n1] = maxsize
    right_arr[n2] = maxsize
    # left_arr.append(maxsize)
    # right_arr.append(maxsize)

    i = 0
    j = 0

    for k in range(lb, rb+1):
        if (left_arr[i] <= right_arr[j]):
            arr[k] = left_arr[i]
            i = i+1
        else:
            arr[k] = right_arr[j]
            j = j+1
            
    


arr = [5, 2, 4, 6, 1, 3]
n = len(arr)

sortedArr=merge_sort(arr, 0, n-1)
# print("Sorted array is:", sortedArr)
