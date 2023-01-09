# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return the maximum number of points that lie on the same straight line.
from math import gcd
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # 通过斜率&与坐标轴交点确认唯一直线
        # lines = {}
        #
        # n = len(points)
        # if len(points) <= 2:
        #     return n
        #
        # res = 0
        # for i in range(n):
        #     for j in range(i + 1, n):
        #         delta_x, delta_y = points[j][0] - points[i][0], points[j][1] - points[i][1]
        #         cd = gcd(delta_x, delta_y)
        #         delta_x, delta_y = int(delta_x / cd), int(delta_y / cd)
        #         if delta_x == 0:
        #             axis_intersection = points[j][0]
        #             delta_y = abs(delta_y)
        #         else:
        #             delta_x, delta_y = (-delta_x, -delta_y) if delta_x < 0 else (delta_x, delta_y)
        #             axis_intersection = points[i][1] - (points[i][0]) * delta_y / delta_x
        #         line = (delta_x, delta_y, axis_intersection)
        #         if line in lines:
        #             lines[line].add(tuple(points[j]))
        #         else:
        #             lines[line] = set([tuple(points[i]), tuple(points[j])])
        #         res = max(res, len(lines[line]))
        #
        #     if res >= (n - i):
        #         break

        # 通过斜率和起点确定唯一直线，仅看起点右侧的点
        # 为此，先对points排序
        n = len(points)
        if len(points) <= 2:
            return n

        points.sort()

        res = 0
        for i in range(n):
            lines = {}
            for j in range(i + 1, n):
                delta_x, delta_y = points[j][0] - points[i][0], points[j][1] - points[i][1]
                cd = gcd(delta_x, delta_y)
                delta_x, delta_y = int(delta_x / cd), int(delta_y / cd)
                line = (delta_x, delta_y)
                if line in lines:
                    lines[line].add(tuple(points[j]))
                else:
                    lines[line] = set([tuple(points[i]), tuple(points[j])])
                res = max(res, len(lines[line]))

            if res > (n - i):
                break

        return res


if __name__ == '__main__':
    points = [[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]
    points = [[4, 5], [4, -1], [4, 0]]
    res = Solution().maxPoints(points)

    print(res)
