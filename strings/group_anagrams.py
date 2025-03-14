'''
Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
Example 2:
Input: s = "rat", t = "car"
Output: false

'''

from collections import Counter
from collections import defaultdict

def is_valid_anagram(str1, str2):
    # compare if all characters are present from 1 str1 in str2.
    # if present then its true anagrams else not..
    map = Counter(str1)
    print(map, sorted(map))
    dap = Counter(str2)
    print(dap, sorted(dap))
    if map == dap:
        print("true")
    else:
        print("false")


def is_anagram(str1, str2):
    ans = Counter(str1) == Counter(str2)
    print("is anagram", ans)
    return ans

#
# def group_anagrams(arr):
#     ana_groups = []
#     for idx, value in enumerate(arr):
#         print(idx, value)
#         tmp = set()
#         for ptr in arr:
#             result = is_anagram(value, ptr)
#             print("found anagram", result, value, ptr)
#             if result:
#                 tmp.add(ptr)
#         tmp.add(value)
#         ana_groups.append(tmp)
#     print(ana_groups)
#     final_set = set()
#     for values in ana_groups:
#         final_set.add(values)
#     print("final ans", final_set)



def group_anagrams(strs):
    print("input", strs)
    anagrams = defaultdict(list)
    print("the anagrams", anagrams)
    for word in strs:
        print("the word", word)
        # createing a tupe as keys need to be of a hasable type which is immutable by nature.. tuples are.
        sorted_word = tuple(sorted(word))  # Sort the characters and use as key
        print("sorted word", sorted_word, word)
        anagrams[sorted_word].append(word)  # Add word to corresponding group
    ans = list(anagrams.values())
    print("the ans", ans)


# O(n*K) v/s O(nlogn) above.. this is more efficient..
def group_anagrams(strs):
    anagrams = defaultdict(list)

    for word in strs:
        count = [0] * 26  # Frequency array for 'a' to 'z'
        for char in word:
            resp = ord(char) - ord('a')
            print("the resp", resp)
            count[resp] += 1
            print("value is here", char, count, ord(char))
        # print("count stuff", count)
        anagrams[tuple(count)].append(word)
    return list(anagrams.values())

# Example usage:
# strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(group_anagrams(strs))


strs = ["eat","tea","tan","ate","nat","bat"]
strs = ["rat", "tar", "cat"]
group_anagrams(strs)
# is_anagram("anagram", "nagaram")
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
#
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
