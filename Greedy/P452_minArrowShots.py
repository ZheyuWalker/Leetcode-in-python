# here are some spherical balloons taped onto a flat wall that represents the XY-plane.
# The balloons are represented as a 2D integer array points where points[i] = [xstart, xend] denotes a balloon
# whose horizontal diameter stretches between xstart and xend. You do not know the exact y-coordinates of the balloons.
#
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
# A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot. A shot arrow keeps traveling up infinitely,
# bursting any balloons in its path.
#
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.


from typing import List


def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort()
    n = len(points)

    if n == 1:
        return 1

    i = 1
    left_bound, right_bound = points[0]
    cnt = 0
    while i < n:
        if points[i][0] <= right_bound:
            left_bound = points[i][0]
            right_bound = min(right_bound, points[i][1])
            i += 1
        else:
            cnt += 1
            left_bound, right_bound = points[i]

    return cnt + 1


if __name__ == '__main__':
    points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
    res = findMinArrowShots(points)
    print(res)
