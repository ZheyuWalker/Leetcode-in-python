# You are given a 0-indexed integer array nums of length n.
# The average difference of the index i is the absolute difference between the average of the first i + 1 elements
# of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.
#
# Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.
# Note:
# The absolute difference of two numbers is the absolute value of their difference.
# The average of n elements is the sum of the n elements divided (integer division) by n.
# The average of 0 elements is considered to be 0.
from typing import List


class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return 0

        front, rear = 0, sum(nums)
        min_diff = abs(rear)
        res = 0
        for i in range(n):
            front += nums[i]
            rear -= nums[i]
            front_mean = front // (i + 1)
            rear_mean = rear // (n - i - 1) if i < n - 1 else 0
            diff = abs(front_mean - rear_mean)
            if diff < min_diff:
                res = i
                min_diff = diff
        return res
