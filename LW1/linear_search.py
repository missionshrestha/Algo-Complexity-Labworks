def linear_search(arr, x):

    n = len(arr)  
    for i in range(n):  
        if arr[i] == x:  
            return i  
    return -1  


""" # Example 
arr = [5, 2, 8, 10, 6]
x = 8
result = linear_search(arr, x)
if result == -1:
    print(f"{x} is not found in the array.")
else:
    print(f"{x} is found at index {result} in the array.") """
