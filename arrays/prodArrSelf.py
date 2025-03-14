'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.


Example 1:

Input: nums = [1,2,3,4]
ans = [ 1, 1, 1, 1]

prefix product = 1 ,
suffix product = 1
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]



'''
def array_product(arr):
    n = len(arr)
    answer = [1] * n
    prefix_product = 1
    for i in range(n):
        answer[i] = prefix_product
        prefix_product = prefix_product * arr[i]
    suffix_product = 1
    print("prefix array is ", answer)
    # rev iterate...
    for i in range(n-1, -1, -1):
        print("answer i and suffix", answer[i], suffix_product)
        answer[i] = answer[i] * suffix_product
        suffix_product = suffix_product * arr[i]
    print(answer)

if __name__ == '__main__':
    arr = [1,2,3,4]
    # create prefix and sufffix arrays and multiple them..
    # [ 1 , 1, 2, 6 ]
    # [ 24, 12, 4, 1]
    array_product(arr)