# knapsack problem..


'''

'''
def knapsack_01(values, weights, capacity):
    n = len(values)
    # Step 1: Create a DP table initialized with 0
    table = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    print("the dp table", table)
    # Step 2: Build the DP table
    for i in range(n + 1):  # Iterate through items
        for w in range(capacity + 1):  # Iterate through weights
            if i == 0 or w == 0:  # Base case: No items or zero capacity
                table[i][w] = 0
            elif weights[i - 1] <= w:  # If the item can be added without exceeding capacity
                # Max of including the item or excluding it
                table[i][w] = max(
                    values[i - 1] + table[i - 1][w - weights[i - 1]],  # Include item
                    table[i - 1][w]  # Exclude item
                )
            else:
                # If the item's weight exceeds the current capacity, exclude it
                table[i][w] = table[i - 1][w]

    # Step 3: Return the maximum value we can get with the given capacity
    return table[n][capacity]

# Example usage
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50
result = knapsack_01(values, weights, capacity)
print(f"Maximum value in the knapsack: {result}")
