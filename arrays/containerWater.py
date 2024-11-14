'''
Water container problem
find the max container...
'''


def water_container(arr):
    n = len(arr)
    area = 0
    for i in range(n):
        for j in range(i + 1, n):
            area = max(area, min(arr[j], arr[i]) * (j - i))
    print("final area", area)


def water_container_optimal(arr):
    n = len(arr)
    left = 0
    right = n - 1
    # keep an initial area. and work from their..
    area = 0
    # measure between both sides...
    while left != right:
        area = max(area, min(arr[left], arr[right]) * (right - left))
        # move is line hieght is smaller...
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1
    print("optimal area is..", area)


if __name__ == '__main__':
    arr = [3, 1, 2, 4, 5]
    water_container_optimal(arr)
