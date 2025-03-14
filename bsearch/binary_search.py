def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            print("found the target", arr[mid])
            break
        elif arr[mid] < target:
            left = mid + 1
            # right half
        else:
            right = mid - 1
            # left half

nums = [2, 1, 4, 1, 4, 5, 0, 13, 9]
nums_srt = sorted(nums)
print(nums_srt)
target = 9
binary_search(nums_srt, 9)
# [ 1 , 2, 3, 4, 5]