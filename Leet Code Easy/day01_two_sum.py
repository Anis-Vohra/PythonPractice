# Problem: Two Sum
# Link: https://leetcode.com/problems/two-sum/
# Date: 7/2/2025
# Level: Easy
# Tags: Array, Hash Table
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Use a hash map to store the complement of each number. If the complement is found, return the indices.

def two_sum(nums, target):
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i

# Example usage
nums = [2, 7, 12 , 15, 34, 68, 754]
target = 756
result = two_sum(nums, target)
print(f"The indices of two numbers in nums that add up to {target}: {result}")

# Test edge cases
if __name__ == "__main__":
    test_cases = [
        ([3, 3], 6),
        ([1, 2, 3], 7),
        ([-1, 0, 1, 2], 1),
        ([1, 2, 3, 4, 4], 8),
        ([5], 10),
        ([], 0),
        ([1000000, 2000000], 3000000)
    ]
print("Edge Cases:")

# Loop through each test case in the list
for nums, target in test_cases:

    # Unpack the tuple into nums (list of numbers) and target (integer)
    # Call the two_sum function with the current test case
    result = two_sum(nums, target)
    
    # Print the inputs and the result in a readable format
    print(f"Input: nums={nums}, target={target} → Output: {result}")