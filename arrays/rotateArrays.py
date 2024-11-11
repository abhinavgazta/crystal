def rotate_array_single(arr, k):
    '''
    logic is
    iterate till arr len...
    arr[i+1] = arr[i]
    T = O(n)
    S = O(1)
    '''
    arr_len = len(arr)
    last_elen = arr[arr_len-1]
    for i in range(arr_len - 1, 0, -1):
        arr[i] = arr[i-1]
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

def rotate_generic(arr, k):
    pass

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 1
    print("some data", arr[3], arr[6])
    # rotate_array_single(arr, k)
    arr_one = [1, 2, 3, 4, 5, 6, 7]
    rotate_array(arr_one, 2)
