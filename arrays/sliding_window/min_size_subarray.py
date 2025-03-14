'''

Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target.
If there is no such subarray, return 0 instead.

'''


def min_size_subarray(arr, target):
    ptr1 = 0
    curr_sum = 0
    min_len = float('inf')

    for ptr2 in range(len(arr)):
        curr_sum += arr[ptr2]
        print("values", curr_sum, ptr2)
        while curr_sum >= target:
            min_len = min(min_len, ptr2 - ptr1 + 1)
            print("exceeedd ", curr_sum, min_len)
            curr_sum = curr_sum - arr[ptr1]
            ptr1 += 1
    return min_len if min_len != float('inf') else 0


# logic .. find all subarrays..whose sum is 7..
# find the one with min len..
#
#
nums = [2, 3, 1, 2, 4, 3]
target = 7
print("ans..."  , min_size_subarray(nums, target))
