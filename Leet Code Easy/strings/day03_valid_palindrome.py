# Problem: Valid Palindrome
# Link: https://leetcode.com/problems/valid-palindrome/
# Date: 7/3/2025
# Level: Easy
# Tags: String, Two Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Approach: Use two pointers and skip non-alphanumeric characters while comparing characters case-insensitively.
# Fun Fact: Question from my first ever technical interview - Did not get the job XD

# Define a function that takes in a string s
def is_palindrome(s):
    # Initialize the two pointers: left at the start, right at the end
    left, right = 0, len(s) - 1
    # Loop until the pointers meet in the middle
    while left < right:
        # Skip characters on the left that aren't letters or numbers
        while left < right and not s[left].isalnum():
            left += 1
        # Skip characters on the right that aren't letters or numbers
        while left < right and not s[right].isalnum():
            right -= 1
        # Compare the lowercase version of the characters at each pointer
        if s[left].lower() != s[right].lower():
            return False  # If they don't match, it's not a palindrome
        # Move both pointers inward
        left += 1
        right -= 1
    # If we made it through the loop, it's a valid palindrome
    return True

# Example usage
print(is_palindrome("A man, a plan, a canal: Panama"))

# Additional test cases
if __name__ == "__main__":
    test_cases = [
        ("", True),
        (" ", True),
        ("a", True),
        ("aa", True),
        ("ab", False),
        ("racecar", True),
        ("No lemon, no melon", True),
        ("Was it a car or a cat I saw?", True),
        ("0P", False),
        ("Able was I, I saw elba", True)
    ]
    
print("Edge Cases:")
    
# Loop through each test case in the list
for s, expected in test_cases:
    
    # Unpack the tuple into s
    # Call the is_palindrome function with the current test case
    result = is_palindrome(s)
    
    # Print the inputs and the result in a readable format
    print(f"Input: '{s}' → Output: {result} | Expected: {expected} | {'Pass' if result == expected else 'Fail'}")