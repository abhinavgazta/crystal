'''
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
..............................................................
..............................................................
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
'''


def remove_duplicates_inplace(arr):
    n = len(arr)
    idx = 1
    for i in range(1, n):
        if arr[i] != arr[i - 1]:
            arr[idx] = arr[i]
            idx += 1
            print(arr)
    print("total idx which has no duplicates in place..", idx)
    for i in range(idx):
        print(arr[i])


if __name__ == '__main__':
    arr = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    arr1 = [1, 2, 2, 3, 4, 4, 4, 5, 5]
    remove_duplicates_inplace(arr)
