'''
Input: intervals =
 [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
logic if arr_0[1] >
'''


def merge_intervals(arr):
    arr.sort()
    n = len(arr) - 1
    merger = []
    idx = 0
    while idx < n:
        if arr[idx][1] >= arr[idx + 1][0]:
            merger.append([arr[idx][0], arr[idx + 1][1]])
            idx += 1
        else:
            merger.append(arr[idx])
            if n - idx == 1:
                merger.append(arr[idx + 1])
        idx += 1
    print("merged...", merger)


# correct merge interval solution... as it handles edge cases....
def merge_interval_correct(arr):
    # return size of in place merged array...
    arr.sort()
    residx = 0
    for i in range(1, len(arr)):
        if arr[residx][1] >= arr[i][0]:
            arr[residx][1] = max(arr[residx][1], arr[i][1])
        else:
            residx += 1
            arr[residx] = arr[i]
        print("values....", residx, arr[residx], arr[i])
    return residx + 1


# good solution to the problem.. solves most of the edge cases as well..
def merge_interval_simple(arr):
    arr.sort()
    print("sorted array", arr)
    # [[1, 5], [2, 4], [4, 6], [7, 8]]
    res = [arr[0]]
    for i in range(1, len(arr)):
        last = res[-1]
        curr = arr[i]
        print("data", last, curr)
        if curr[0] < last[1]:
            last[1] = max(last[1], curr[1])
        else:
            res.append(curr)
    print("final merged interval", res)


if __name__ == '__main__':
    # sorting is important..
    # then moving till merging al overlapping intervals..by comparison.
    # O(n*logn) and O(n) time / space..
    # arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
    arr = [[7, 8], [1, 5], [2, 4], [4, 6]]
    # arr = [[1, 4], [4, 5]]
    merge_interval_simple(arr)
    #  merged the array...
