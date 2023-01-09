# You are given an integer array nums.
# You should move each element of nums into one of the two arrays A and B such that A and B are non-empty,
# and average(A) == average(B).
#
# Return true if it is possible to achieve that and false otherwise.
# Note that for an array arr, average(arr) is the sum of all the elements of arr over the length of arr.


class Solution:
    def splitArraySameAverage(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1:
            return False
        if n == 2:
            return True if nums[0] == nums[1] else False

        nums.sort()

        part_a, part_b = [], []

