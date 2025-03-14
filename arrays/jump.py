# You are given an integer array nums.
# You are initially positioned at the array's first index,
# and each element in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.

'''
Example 1:
Input: nums = [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.


You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
0 <= j <= nums[i] and
i + j < n

'''


# def jumpCheck(arr):
#     # to check if u can reach last element.
#     # [ 2 , 3, 1, 1, 4]
#     idx = 0
#     dist_final_idx = 0
#     last_idx = len(arr) - 1
#     last_elem = arr[last_idx]
#     check = False
#     # check for loop in array.. if loop then cannot reach last index..
#     # fast and slow ptr method..
#     for elem in arr:
#         print("elem", elem)
#         jmp_elem = arr[elem]
#         dist_new_idx = last_idx - elem
#         if dist_new_idx > dist_final_idx:
#
#     return check

def canJump(nums):
    maxReach = 0
    last_index = len(nums) - 1
    for i in range(len(nums)):
        print(i, nums[i], maxReach)
        # so this makes sense as ou cant exceeed this..
        if i > maxReach:
            return False
        # take max of index and value at that index and prev maxReach and  after compare with last index of array..
        maxReach = max(maxReach, i + nums[i])
        if maxReach >= last_index:
            return True
    return True


def canJumpFinal(nums):
    maxReach = 0
    countMinJump = 0
    last_index = len(nums) - 1
    for i in range(len(nums)):
        print(i, nums[i], maxReach)
        # so this makes sense as ou cant exceeed this..
        if i > maxReach:
            return False
        # take max of index and value at that index and prev maxReach and  after compare with last index of array..
        maxReach = max(maxReach, i + nums[i])
        countMinJump += 1
        if maxReach >= last_index:
            return True, countMinJump
    return True, countMinJump

if __name__ == '__main__':
    arr = [2, 3, 1, 1, 4]
    arr1 = [3, 2, 1, 0, 4]
    bo = [2,3,0,1,4]
    # print(jumpCheck(arr))
    print("final result", canJumpFinal(bo))
