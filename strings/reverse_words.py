'''
Given an input string s, reverse the order of the words.

A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.

Return a string of the words in reverse order concatenated by a single space.

Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.



Example 1:

Input: s = "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: s = "  hello world  "
Output: "world hello"
Explanation: Your reversed string should not contain leading or trailing spaces.



'''


def reverse_words(strs):
    strs_new = strs.strip()
    # print(strs_new)
    split_arr = strs_new.split(" ")
    # new_arr = list(reversed(split_arr))
    new_arr = split_arr[::-1]
    # print(new_arr)
    ans = " ".join(new_arr)
    print(ans)


if __name__ == '__main__':
    s = "  the sky is blue "
    reverse_words(s)