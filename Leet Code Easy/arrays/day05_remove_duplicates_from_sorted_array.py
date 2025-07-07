# Problem: Remove Duplicates from Sorted Array
# Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Date: 7/5/2025
# Level: Easy
# Tags: Array, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Use two pointers to shift unique values to the front of the list.

def remove_dups(nums):
    # If the input list is empty, there is no elements to process
    if not nums:
        return 0
   
    # The slow pointer keeps track of the index where the next unique number should go
    slow = 1
  
    # Start the loop from the second element (index 1)
    for fast in range(1, len(nums)):
        # Compare current number to the one just before it
        # If they are different, it means we found a new unique number
        if nums[fast] != nums[fast - 1]:
            # Copy the new unique number to the slow pointer position
            nums[slow] = nums[fast]
            # Move the slow pointer to the next available spot for a future unique number
            slow += 1
   
    # After the loop finishes, slow is the count of unique elements
    # The first slow elements in numbs are now the deduplicated values
    return slow

# Example usage
if __name__ == "__main__":
    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([], 0, []),
        ([1], 1, [1]),
        ([1, 2], 2, [1, 2]),
        ([1, 1, 1, 1], 1, [1]),
    ]

# Loop through each test case in the list
    for nums, expected_k, expected_prefix in test_cases:
        original = nums[:]
        k = remove_dups(nums)
        print(f"Input: {original} → k = {k}, nums[:k] = {nums[:k]} | Expected: {expected_prefix}")
    