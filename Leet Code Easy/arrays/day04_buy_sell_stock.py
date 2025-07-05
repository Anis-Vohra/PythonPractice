# Problem: Best Time to Buy and Sell Stock
# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Date: 7/4/2025
# Level: Easy
# Tags: Array, Greedy, Dynamic Programming
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Track the minimum price so far and the max profit at each step.

# Define a function that has a list of prices
def max_profit(prices):
    # We haven’t seen any prices yet, so assume the worst
    # The price is infinitely high.
    min_price = float('inf')
    # We haven’t made any trades yet, so our profit is 0
    max_profit = 0
    # Loop through each days prices
    for price in prices:
        # Update the min price if lower price is found
        if price < min_price:
            min_price = price
        # Calculate the profit if sold today and update max profit if its better
        elif price - min_price > max_profit:
            max_profit = price - min_price
    #End of loop
    return max_profit

# Example usage
if __name__ == "__main__":
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([2, 4, 1], 2),
        ([1, 2], 1),
        ([1], 0),
        ([], 0)
    ]

# Loop through each test case in the list
for prices, expected in test_cases:
    # Unpack the tuple into prices
    # Call the max_profit function with the current test case
    result = max_profit(prices)

    # Print the inputs and the result in a readable format
    print(f"Prices: {prices} → Max Profit: {result} | Expected: {expected}")