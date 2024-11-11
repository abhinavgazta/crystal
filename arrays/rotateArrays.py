def rotate_array_single(arr, k):
    '''
    logic is
    iterate till arr len...
    arr[i+1] = arr[i]
    T = O(n)
    S = O(1)
    '''
    arr_len = len(arr)
    last_elen = arr[arr_len - 1]
    for i in range(arr_len - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last_elen
    print("updated arr", arr)


def rotate_array(arr, k):
    '''

    two pointer approach to
    '''
    n = len(arr)
    i = 0
    j = n - 1
    while i != j:
        arr[i], arr[j] = arr[j], arr[i]
        i = i + 1
    print("rotated array", arr)


def rotate_generic(arr, d):
    # rotate to left k times...
    # [1, 2, 3, 4, 5, 6]
    n = len(arr)
    temp = [0] * n
    d %= n
    # copy last n-d elements into temp array..
    for i in range(n - d):
        temp[i] = arr[d + i]
    print("first temp array", temp)
    # copy first d elements to back of temp array
    for i in range(d):
        temp[n - d + i] = arr[i]
    print("after temp array", temp)

    # copy temp into arr
    for i in range(n):
        arr[i] = temp[i]
    print("rotate array counter clk wise", arr)


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


def rotate_array_work(arr, d):
    '''

    works for both left or right rotation
    sequence right -: first reverse all, then reverse first and then last.
    for left rotation...
    first rotate
    :param arr:
    :param d:
    :return:
    '''
    n = len(arr)
    d %= n
    '''
    left rotation sequence...  
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    reverse(arr, 0, n - 1)
    '''
    reverse(arr, 0, n - 1)
    reverse(arr, 0, d - 1)
    reverse(arr, d, n - 1)
    print("rotated array", arr)


if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 5, 6, 7]
    # k = 1
    # print("some data", arr[3], arr[6])
    # # rotate_array_single(arr, k)
    # arr_one = [1, 2, 3, 4, 5, 6, 7]
    # rotate_array(arr_one, 2)
    # print("testing generic rotation left..... ")
    arr = [1, 2, 3, 4, 5, 6]
    # rotate_generic(arr, d=5)
    rotate_array_work(arr, d=1)
