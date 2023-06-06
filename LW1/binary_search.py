from math import floor
def binary_search(values, target, left, right): 
    if (left > right): 
        return -1 
    midpoint = floor((left+right)/2) 
    if (values[midpoint] == target): 
        return midpoint 
    elif (values[midpoint] < target): 
        return binary_search(values, target, midpoint+1, right) 
    else: 
        return binary_search(values, target, left, midpoint-1)


""" 
# Example 
arr = [2, 5, 6, 8, 10]
x = 8
result = binary_search(arr, x,0,len(arr))
if result == -1:
    print(f"{x} is not found in the array.")
else:
    print(f"{x} is found at index {result} in the array.")
 """