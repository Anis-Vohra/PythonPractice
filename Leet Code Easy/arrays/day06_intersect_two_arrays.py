# Problem: Intersection of Two Arrays II
# Link: https://leetcode.com/problems/intersection-of-two-arrays-ii/
# Date: 7/5/2025
# Level: Easy
# Tags: Array, Hash Map, Two-Pointers
# Time Complexity: O(n + m)
# Space Complexity: O(min(n, m))
# Approach: Use a dictionary to store the frequency of elements from one array, then match with the second array.

def intersect(nums1, nums2):
    # Make sure we alwaure the the map from the smaller array, for better space ussage.
    if len(nums1) < len(nums2):
        nums1, nums2 = nums2, nums1

    # Create a frequency map from nums1
    freq_map = {}
    for num in nums1:
        # If the number already exists, increase its count
        if num in freq_map:
            freq_map[num] += 1
        else:
            # Otherwise, add iot to the map with count 1
            freq_map[num] = 1
  
    # Create the result list to store common elements:
    result = []
   
    # Iterate through nums2 and check if the elemnt exists in the freq_map
    for num in nums2:
        # Only add to result if this number exists in freq_map and still has a count > 0
        if num in freq_map and freq_map[num] > 0:
            result.append(num)
            # Decrease the count so we dont reuse this number again
            freq_map[num] -= 1

    # End of loop
    return result

# Example usage
if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 1], [2, 2], [2, 2]),
        ([4, 9, 5], [9, 4, 9, 8, 4], [4, 9]),  # [9, 4] is also valid
        ([1, 2], [1, 1], [1]),
        ([1], [1, 2, 1], [1]),
        ([1, 2, 3], [4, 5, 6], []),  # No intersection
        ([], [1, 2, 3], []),
        ([1, 2, 2], [], []),
    ]

print("Edge Cases:")

# Loop through each test case in the list
for nums1, nums2, expected in test_cases:
        output = intersect(nums1, nums2)
        print(f"nums1={nums1}, nums2={nums2} → intersection={output} | expected similar to: {expected}")