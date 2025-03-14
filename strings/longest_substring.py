"""
Given a string s, find the length of the longest substring without duplicate characters.
"""


def length_of_longest_substring(s):
    char_set = set()  # To track unique characters
    left = 0
    max_length = 0
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])  # Remove leftmost character
            left += 1  # Move left pointer forward
        char_set.add(s[right])  # Add current character
        max_length = max(max_length, right - left + 1)  # Update max length
    print("longest char set is", char_set, len(char_set))
    return max_length


# Example usage:
s = "abcabcbbghijk"
print(length_of_longest_substring(s))


def longest_sub(strs):
    char_set = set()
    left = 0
    for right in range(len(strs)):
        while strs[right] in char_set:
            # move the left pointer and remove left most element...
            char_set.remove(strs[left])
            left += 1
        char_set.add(strs[right])
    print("final charset", sorted(char_set))

s = "abcabcbbghijks"
longest_sub(s)