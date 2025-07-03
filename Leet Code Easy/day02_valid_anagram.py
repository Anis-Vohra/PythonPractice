# Problem: Valid Anagram
# Link: https://leetcode.com/problems/valid-anagram/
# Date: 7/2/2025
# Level: Easy
# Tags: Hash Table, String
# Time Complexity: O(n)
# Space Complexity: O(n)
# Approach: Count frequency of each character in both strings and compare.

# Define a function that takes two strings, s and t
def is_anagram(s, t):
    # If s and t are not the same length, they can't be anagrams
    if len(s) != len(t):
        return False
    # Create an empty dictionary to count characters in s
    char_count = {}
    # Count the frequency of each character in string s
    for char in s:
        # If the character is already in the dictionary, increment it. If not, set it to 1
        char_count[char] = char_count.get(char, 0) + 1
    # Now iterate over each character in t
    for char in t:
        # If the character doesn't exist in the dictionary, it's not an anagram
        if char not in char_count:
            return False
        # Subtract 1 from the count for that character
        char_count[char] -= 1
        # If the count goes below 0, there are too many of that character in t
        return False
    # If all checks passed, s and t are anagrams
    return True

#Example usage
s = "listen"
t = "silent"
result = is_anagram(s, t)
print(f"Input: s='{s}', t='{t}' → Output: {result}")

#Test Cases
if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("", "", True),
        ("a", "a", True),
        ("ab", "ba", True),
        ("ab", "abc", False),
        ("aabbcc", "abcabc", True),
        ("aacc", "ccac", False)
    ]

print("Edge Cases:")

# Loop through each test case in the list
for s, t, expected in test_cases:
    
    # Unpack the tuple into s and t
    # Call the is_anargam function with the current test case
    result = is_anagram(s, t)

    # Print the inputs and the result in a readable format
    print(f"Input: s ='{s}', t ='{t}' → Output: {result} | Expected: {expected} | {'Pass' if result == expected else 'Fail'}")