# Problem: Find the Index of the First Occurrence in a String
# Link: https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Date: 7/5/2025
# Level: Easy
# Tags: String, Two Pointers
# Time Complexity: O(n * m)
# Space Complexity: O(1)

def strStr(haystack, needle):
    n = len(needle)
    m = len(haystack)

    # Check for empty needle
    if m == 0:
        return 0
    
    # Check every possible starting point in the haystack
    for i in range(n - m + 1):
        # Compare the slice of the haystack to the needle
        if haystack[i:i + m] == needle:
            # Match found
            return i 

    # No match found
    return -1

if __name__ == "__main__":
    test_cases = [
        ("hello", "ll", 2),
        ("aaaaa", "bba", -1),
        ("", "", 0),
        ("abc", "", 0),
        ("abc", "c", 2),
        ("mississippi", "issip", 4),
    ]

    for haystack, needle, expected in test_cases:
        result = strStr(haystack, needle)
        print(f"haystack='{haystack}', needle='{needle}' → Output: {result} | Expected: {expected}")


