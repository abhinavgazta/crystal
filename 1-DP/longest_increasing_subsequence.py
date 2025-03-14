# longest increasing subsequence....
import bisect


# O(n2) solution...
def longest_increasing_subsequence(arr):
    if not nums:
        return 0
    n = len(arr)
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j]+1)
    print("ANS", max(dp))


def length_of_lis(nums):
    if not nums:
        return 0

    lis = []

    for num in nums:
        pos = bisect.bisect_left(lis, num)
        print("the pos", pos, "num", num, "len", len(lis))
        if pos == len(lis):
            lis.append(num)  # New larger element → Extend the subsequence
        else:
            lis[pos] = num  # Replace element to maintain the smallest possible value
    return len(lis)


# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
result = length_of_lis(nums)
print(f"Length of Longest Increasing Subsequence: {result}")

nums = [10,9,2,5,3,7,101,18]
# ans = 4, [2,3,7,101]
longest_increasing_subsequence(nums)
