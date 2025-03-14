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


def rotate(nums, k):
    n = len(nums)
    k %= n  # Handle cases where k > n

    def reverse(left, right):
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    # Step 1: Reverse the entire array
    # left = 0, right = n - 1
    reverse(0, n - 1)
    # left = 0, right = k - 1
    # Step 2: Reverse the first k elements
    reverse(0, k - 1)
    #  left = k , right = n - 1
    # Step 3: Reverse the remaining elements
    reverse(k, n - 1)


def reverseCode(arr, left, right):
    while left != right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

if __name__ == '__main__':
    # arr = [1, 2, 3, 4, 5, 6, 7]
    # [ 1 , 2, 3 ] left = 0 , right = n-1
    # [ 3, 1, 2 ] left = 0, right = k-1
    # k = 1  left = k , right n-1
    # print("some data", arr[3], arr[6])
    # # rotate_array_single(arr, k)
    # arr_one = [1, 2, 3, 4, 5, 6, 7]
    # rotate_array(arr_one, 2)
    # print("testing generic rotation left..... ")
    # arr = [1, 2, 3, 4, 5, 6]
    # rotate_generic(arr, d=5)
    # rotate_array_work(arr, d=1)
    # Example usage:
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate(nums, 10)
    print(nums)  # Output: [5, 6, 7, 1, 2, 3, 4]
    n = len(nums)
    bot = reverseCode(nums, 0, n-1)
    bot = reverseCode(nums, k-1)
    reverseCode(k, n-1)
    print(bot)