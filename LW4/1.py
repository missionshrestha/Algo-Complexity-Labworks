def knapsack_brute_force(W, wt, val, n):
    max_value = 0
    max_combination = []
    # We generate all possible combinations of items using binary representation.
    # There will be 2^n possible combinations including the empty bag.
    for i in range(2**n):
        current_weight = 0
        current_value = 0
        current_combination = []
        # We check each item to see if it is included in the current combination.
        for j in range(n):
            # If the jth bit of the binary representation of i is 1, that means we include the jth item in the combination.
            if i & (1 << j):
                current_weight += wt[j]
                current_value += val[j]
                current_combination.append(j)
        # We check if the total weight of the current combination is less than or equal to the maximum weight capacity.
        if current_weight <= W and current_value > max_value:
            # If it is, we update the maximum value seen so far and the corresponding combination of items.
            max_value = current_value
            max_combination = current_combination
    # We return the maximum value and the corresponding combination of items that can be obtained with the given weight capacity and items using brute force.
    return max_value, max_combination


# Example usage:
W = 50  # Maximum weight capacity
wt = [10, 20, 30]  # Weight of each item
val = [60, 100, 120]  # Value of each item
n = len(wt)  # Number of items

max_value, max_combination = knapsack_brute_force(W, wt, val, n)
print("Maximum value that can be obtained with the given weight capacity and items:", max_value)
print("Combination of items that can achieve the maximum value:", max_combination)
