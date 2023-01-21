# Given an integer array nums, return all the different possible non-decreasing subsequences of the given array with
# at least two elements. You may return the answer in any order.

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        res = [[nums[0]]]
        for num in nums[1:]:
            res += [_ + [num] for _ in res if _[-1] <= num]
            res.append([num])

        return list(set([tuple(_) for _ in res if len(_) > 1]))


if __name__ == '__main__':
    # x = [4, 6, 7, 7]
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 1, 1, 1, 1]
    res = Solution().findSubsequences(x)
    res2 = Solution().find2(x)
    print(res)
