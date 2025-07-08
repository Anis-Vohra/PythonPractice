# Problem: Contains Duplicate
# Link: https://leetcode.com/problems/contains-duplicate/
# Date: 7/5/2025
# Level: Easy
# Tags: Array, Hash Set
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Use a set to track seen values. Return early if a duplicate is found.

def contains_duplicate(nums):
    # Create an empty set to keep track of seen numbers
    seen = set()

    # Loop through each number in the input list
    for num in nums:
        # If the number is already in the set, we've found a duplicate
        if num in seen:
            return True
        # Otherwise, add the number to the set
        seen.add(num)

    # If we finish the loop without finding duplicates, return False
    return False

if __name__ == "__main__":
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1], False),
        ([], False),
    ]

    for nums, expected in test_cases:
        result = contains_duplicate(nums)
        print(f"Input: {nums} → Output: {result} | Expected: {expected}")
