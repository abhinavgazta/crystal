'''

Given an integer array nums, move all 0's to the end of it
while maintaining the relative order of the non-zero elements.

'''


def move_zeros(arr):
    n  = len(arr)
    for i in range(0 , n-1):
        if arr[i] != 0:
            


if __name__ == '__main__':
    arr = [0, 1, 0, 3, 12]
    move_zeros(arr)
