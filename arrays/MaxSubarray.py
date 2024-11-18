'''
Max subarray
Given an integer array nums, find the
subarray with the largest sum, and return its sum.
'''


def maxSubArray(arr):
    n = len(arr)
    maxSum = arr[0]
    currSum = arr[0]
    for i in range(1, n):
        currSum = max(currSum + arr[i], arr[i])
        maxSum = max(maxSum, currSum)
    print("final value", maxSum)
    return maxSum


if __name__ == '__main__':
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = maxSubArray(nums1)
    print("Maximum subarray sum for nums1:", result1)  # Expected output: 6

    # Test case 2
    nums2 = [1]
    result2 = maxSubArray(nums2)
    print("Maximum subarray sum for nums2:", result2)  # Expected output: 1

    # Test case 3
    nums3 = [5, 4, -1, 7, 8]
    result3 = maxSubArray(nums3)  # expected output : 23
