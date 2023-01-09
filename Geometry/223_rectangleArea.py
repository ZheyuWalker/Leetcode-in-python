'''
Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

'''

class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        if ax1 < bx1:
            left_box_x = (ax1, ax2)
            right_box_x = (bx1, bx2)
        else:
            left_box_x = (bx1, bx2)
            right_box_x = (ax1, ax2)

        if ay1 < by1:
            down_box_y = (ay1, ay2)
            up_box_y = (by1, by2)
        else:
            down_box_y = (by1, by2)
            up_box_y = (ay1, ay2)

        area1 = (ay2-ay1) * (ax2-ax1)
        area2 = (by2-by1) * (bx2-bx1)

        # 左框的右边界 < 右框的左边界 或 下框的上边界 < 上框的下边界
        if left_box_x[1] <= right_box_x[0] or down_box_y[1] <= up_box_y[0]:
            common_area = 0
        else:
            x_len = min(left_box_x[1], right_box_x[1]) - right_box_x[0]
            y_len = min(down_box_y[1], up_box_y[1]) - up_box_y[0]
            common_area = x_len * y_len

        return area1 + area2 - common_area
