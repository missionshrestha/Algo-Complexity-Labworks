def knapsack_brute_force(max_capacity, weight, value, n):
    max_value = 0

    for i in range(2**n):
        current_value = 0
        current_weight = 0

        print("\n")
        for j in range(n):
            a = i & 1 << j
            print(a)


knapsack_brute_force(5, [10, 20, 30], [60, 100, 120], 3)
