'''

Code
Testcase
Test Result
Test Result
452. Minimum Number of Arrows to Burst Balloons
Medium
Topics
Companies
There are some spherical balloons taped onto a flat wall that represents the XY-plane. The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.

Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis. A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend. There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely, bursting any balloons in its path.

Given the array points, return the minimum number of arrows that must be shot to burst all balloons.



Example 1:

Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
Example 2:

Input: points = [[1,2],[3,4],[5,6],[7,8]]
Output: 4
Explanation: One arrow needs to be shot for each balloon for a total of 4 arrows.
Example 3:

Input: points = [[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 2, bursting the balloons [1,2] and [2,3].
- Shoot an arrow at x = 4, bursting the balloons [3,4] and [4,5].

'''


def burst_balloons(arr):
    # find overlapping intervals.. keep count of how many..
    #  number of arrows to shoot.
    arr.sort()
    print(arr)
    prev = [arr[0]]
    cnt = 0
    for start, end in arr[1:]:
        last_start, last_end = prev[-1]
        if start <= last_end:
            cnt += 1
            prev[-1][1] = max(last_end, end)
        else:
            prev.append([start, end])
    if cnt > 0:
        print("shoot ", cnt - 1)
    else:
        cnt = len(arr)
    print("new merge arrya", prev)
    print("baloons shot", cnt - 1)


def find_min_arrows(points):
    if not points:
        return 0
    # Sort balloons based on their end coordinate (xend)
    points.sort(key=lambda x: x[1])
    print("sorted points", points)
    arrows = 1  # We need at least one arrow to start
    shoot_position = points[0][1]  # Position of the first arrow
    for xstart, xend in points[1:]:
        if xstart > shoot_position:  # If this balloon starts after the last shot
            arrows += 1
            shoot_position = xend  # Shoot a new arrow at the current balloon's end

    return arrows


# Example usage:
points = [[10, 16], [2, 8], [1, 6], [7, 12]]
print(find_min_arrows(points))  # Output: 2

# arr = [[10,16],[2,8],[1,6],[7,12]]
# pot = [[1,2],[3,4],[5,6],[7,8]]
# cat = [[1,2],[2,3],[3,4],[4,5]]
# burst_balloons(cat)
