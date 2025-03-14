'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
..............................................................
..............................................................
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
'''


def remove_duplicates(nums):
    if not nums:  # Handle empty list case
        return 0

    k = 0  # Initialize the index for the modified array
    count = 1  # Initialize the count for the current element

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            nums[k] = nums[i]
            k += 1

    # Place the first element (which was skipped in the loop)
    if k == 0 or nums[0] != nums[1]:  # handle edge cases where the first element might be unique
        nums[k] = nums[0]
        k += 1

    gost = []
    for x in range(k):
        gost.append(arr[x])
    print("ghostttt", gost)
    return k

def remove_duplicates_inplace_atmosttwice(arr):
    n = len(arr)
    idx = 0
    count = 1
    for curr in range(1, n):
        if arr[curr] == arr[curr - 1]:
            count += 1
        else:
            count = 1

        if count <= 2:
            arr[idx] = arr[curr]
            idx += 1

    if idx == 0 or arr[0] != arr[1]:  # handle edge cases where the first element might be unique
        arr[idx] = arr[0]
        idx += 1

    print("last two done...", arr)
    narr = []
    for i in a:
        narr.append(arr[i])
        print(arr[i])
    print(narr)


def remove_duplicates_inplace(arr):
    # array is sorted.. so no problem...
    n = len(arr)
    idx = 1  # starting from next...
    for curr in range(1, n):
        if arr[curr] != arr[curr - 1]:
            arr[idx] = arr[curr]
            idx += 1
    print("total idx which has no duplicates in place..", idx)
    newarr = []
    for i in range(idx):
        print(arr[i])
        newarr.append(i)
    return arr, newarr


def removeDuplicates(nums):
    if len(nums) <= 2:
        return len(nums)

    index = 2  # Start from the third element
    for i in range(2, len(nums)):
        if nums[i] != nums[index - 2]:  # Allow at most two occurrences
            nums[index] = nums[i]
            index += 1

    return index  # Length of modified array


# Example usage:


if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    arr1 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    nums1 = [1, 1, 1, 2, 2, 2, 3, 3, 3, 4]
    # remove_duplicates_inplace_atmosttwice(nums1)
    nums = [1, 1, 1, 2, 2, 3]
    new_length = removeDuplicates(arr1)
    print(arr1[:new_length])
    # remove_duplicates(nums1)
    # _, newarr = remove_duplicates_inplace(arr)
    # print(newarr)
