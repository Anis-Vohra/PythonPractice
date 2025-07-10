# Problem: Longest Common Prefix
# Link: https://leetcode.com/problems/longest-common-prefix/
# Date: 7/5/2025
# Level: Easy
# Tags: String
# Time Complexity: O(n * m), where n = number of strings, m = length of shortest string
# Space Complexity: O(1)

def longest_common_prefix(strs):
    if not strs:
        return ""

    # Loop over the characters of the first string
    for i in range(len(strs[0])):
        current_char = strs[0][i]

        # Compare this character with all other strings at the same position
        for word in strs[1:]:
            # If index is out of range or characters don't match
            if i >= len(word) or word[i] != current_char:
                return strs[0][:i]  # Return the prefix up to this point

    return strs[0]  # All characters matched

if __name__ == "__main__":
    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        (["interspecies", "interstellar", "interstate"], "inters"),
        (["a"], "a"),
        (["", "b"], ""),
    ]

    for strs, expected in test_cases:
        result = longest_common_prefix(strs)
        print(f"Input: {strs} → Output: '{result}' | Expected: '{expected}'")
