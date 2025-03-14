"""
Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
Example 3:
Input: nums = [1,0,1,2]
Output: 3
"""

from collections import defaultdict
# solve in order(n)...
# consequtive means difference is 1. 4-3-2-1...
def longest_consecutive_seq(arr):
    # put values as keys into dict..
    # iterate over array and check if diff (value - 1 ) in map..
    # it it exists then increase the count..
    map = defaultdict()
    for k in arr:
        map[k] = 0
    print("map", map.keys())
    cnt = 0
    seq = []
    top = set(arr)
    print("the top", top)
    for values in top:
        if (values - 1) in map.keys():
            cnt += 1
            seq.append(values)
        if (values - 1) == 0 and values in map.keys():
            cnt += 1
            seq.append(values)
    print("ans is here", cnt, seq)


def longest_consecutive(nums):
    num_set = set(nums)  # Convert the array to a set for O(1) lookups
    longest_streak = 0

    for num in num_set:
        if num - 1 not in num_set:  # Check if 'num' is the start of a sequence
            current_num = num
            current_streak = 1
            print("current num", current_num)
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1

            longest_streak = max(longest_streak, current_streak)
    print("longest streak", longest_streak)
    return longest_streak

arr = [100, 4, 200, 1, 3, 2]
# arr = [0,3,7,2,5,8,4,6,0,1]
# arr = [1,0,1,2]
longest_consecutive(arr)
