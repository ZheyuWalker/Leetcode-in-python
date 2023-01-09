# You are given two arrays of integers nums1 and nums2, possibly of different lengths. The values in the arrays are
# between 1 and 6, inclusive.
#
# In one operation, you can change any integer's value in any of the arrays to any value between 1 and 6, inclusive.
#
# Return the minimum number of operations required to make the sum of values in nums1 equal to the sum of values in
# nums2. Return -1​​​​​ if it is not possible to make the sum of the two arrays equal.


from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        l1, l2 = len(nums1), len(nums2)
        if 6 * min(l1, l2) < max(l1, l2):
            return -1

        diff = abs(s1 - s2)
        if diff == 0:
            return 0
        small, large = (nums1, nums2) if s1 < s2 else (nums2, nums1)
        small = [6 - x for x in small if x < 6]
        large = [x - 1 for x in large if x > 1]

        # Solution 1
        # diffs = small + large
        # diffs.sort(reverse=True)
        # i = 0
        # while diff>0:
        #     diff -= diffs[i]
        #     i += 1
        # return i

        # Solution 2
        small.sort()
        large.sort()
        i = 0
        while diff > 0:
            if len(small) and len(large):
                if small[-1] >= large[-1]:
                    diff -= small[-1]
                    small.pop()
                else:
                    diff -= large[-1]
                    large.pop()
                i += 1
            else:
                remain = small if small else large
                while not (not (diff > 0) or not remain):
                    diff -= remain[-1]
                    remain.pop()
                    i += 1

        return i


if __name__ == '__main__':
    nums1 = [1, 2, 6, 4, 1, 5, 4, 6, 5, 4, 4, 6, 6, 4, 3, 3, 1, 2, 1, 6, 2, 2, 4, 2, 5, 5, 3, 1, 4, 2, 2, 1, 4, 4, 5,
             6, 1, 3, 4, 1, 3, 5, 3, 5, 3, 4, 4, 4, 3, 3, 5, 1, 2, 2, 4, 5, 2, 1, 2, 3, 3, 4, 1, 3, 2, 4, 1, 3, 5, 1,
             6, 3, 3, 4, 6, 5, 5, 2, 6, 5, 4, 5]
    nums2 = [6, 3, 4, 6, 4, 3, 6, 4, 2, 4, 5, 5, 1, 1, 3, 2, 1, 1, 4, 2, 5, 1, 5, 6, 6, 2, 1, 3, 4, 6, 4, 6, 3, 6, 1, 1,
             4, 4, 6, 3, 3, 5, 5, 4, 6, 6, 1, 3, 4, 1, 3, 5, 1, 1, 1, 5, 2, 1, 1, 1, 2, 3, 6, 6, 2, 5, 4, 2, 1, 5, 3, 1,
             2, 3, 6, 4, 2, 5, 4, 6, 6, 6, 6, 6, 3, 2, 2, 2, 1, 6, 4, 5, 6, 1, 5, 1, 5, 6, 6, 4, 6, 5, 3, 4, 1, 3, 2, 1,
             5, 1, 1, 1, 2, 3, 6, 6, 6, 4, 6, 3, 6, 4, 4, 6, 3, 6, 3, 6, 2, 6, 5, 1, 1, 6, 4, 3, 4, 2, 5, 3, 3, 5, 2, 3,
             1, 3, 2, 6, 5, 1, 2, 4, 4, 6, 2, 1, 4, 3, 3, 3, 3, 5, 6, 1, 6, 4, 2, 3, 5, 4, 6, 1, 3, 6, 1, 2, 2, 1, 3, 5,
             6, 2, 3, 6, 5, 3, 4, 1, 3, 1, 2, 3, 5, 4, 2, 1, 2, 1, 2, 5, 2, 4, 4, 4, 2, 5, 2, 4, 3, 2, 1, 5, 1, 3, 3, 1,
             1, 1, 1, 6, 1, 3, 6, 2, 3, 6, 3, 3, 4, 5, 2, 1, 3, 3, 4, 1, 4, 3, 4, 4, 3, 2, 1, 4, 5, 2, 1, 2, 5, 6, 1, 5,
             2, 4, 5, 1, 6, 2, 6, 1, 3, 6, 2, 3, 6, 6, 3, 2, 2, 3, 1, 6, 1, 5, 6, 4, 2, 3, 5, 2, 6, 3, 5, 4, 2, 6, 6, 6,
             5, 5, 4, 2, 3, 1, 1, 4, 4, 4, 5, 2, 4, 3, 6, 4, 3, 3, 2, 3, 4, 6, 1, 1, 6, 1, 6, 2, 4, 5, 4, 2, 4, 4, 4, 1,
             1, 1, 1, 3, 4, 1, 2, 5, 1, 2, 1, 4, 5, 6, 4, 6, 4, 3, 1, 6, 5, 5, 2, 1, 1, 1, 1, 6, 5, 5, 3, 2, 2, 2, 2, 6,
             2, 3, 3, 5, 1, 6, 5, 6, 2, 2, 1, 6, 1, 6, 5, 2, 5, 4, 4, 1, 5, 5, 6, 4, 4, 1, 3, 1, 6, 4, 4, 3, 1, 6, 6, 6,
             4, 6, 5, 3, 6, 4, 3, 6, 2, 3, 3, 3, 2, 4, 2, 2, 2, 3, 5, 2, 6, 5, 4, 5, 4, 2, 5, 1, 3, 6, 4, 1, 2, 1, 3, 3,
             3, 3, 1]
    print(Solution().minOperations(nums1, nums2))
