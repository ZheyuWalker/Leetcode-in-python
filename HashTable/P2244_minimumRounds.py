# You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task.
# In each round, you can complete either 2 or 3 tasks of the same difficulty level.
#
# Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.

from collections import Counter
from math import ceil
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        cnt = Counter(tasks).most_common()
        if cnt[-1][1] <= 1:
            return -1

        res = 0
        for _, num in cnt:
            res += ceil(num / 3)

        return res
