'''
Given an integer array nums,
return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums
is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in
 O(n) time and without using the division operation.


Input: nums = [1,2,3,4]
Output: [24,12,8,6]

'''


def product_self(arr):
    product_arr = []
    for idx, data in enumerate(arr):
        product = 1
        for x in arr:
            result = x != arr[idx]
            if result:
                product = product * x
        product_arr.append(product)
    print("the product value...", arr, product_arr)


def optimal_product_self(arr):
    n = len(arr)
    if n == 1:
        return [1]
    left = [1] * n
    right = [1] * n
    prod = [1] * n
    for i in range(1, n):
        left[i] = arr[i - 1] * left[i - 1]
    print("final left arr", left)

    for j in range(n - 2, -1, -1):
        right[j] = right[j + 1] * arr[j + 1]
    print("final right arr", right)

    for i in range(n):
        prod[i] = left[i] * right[i]
    print("final ans", prod)


if __name__ == '__main__':
    # arr = [1, 2, 3, 4]
    arr = [-1, 1, 0, -3, 3]
    arr1 = [10, 3, 5, 6, 2]
    product_self(arr1)
    optimal_product_self(arr1)
