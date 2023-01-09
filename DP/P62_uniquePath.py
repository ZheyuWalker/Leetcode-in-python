import random
import time

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        # line_path_cnt: the num of unique_path (num_path) of mth line and nth columns
        # if m == 1, num_path for any n equals to 1
        line_path_cnt = n * [1]
        # when m > 1
        # since 2nd line, num_path[i][j] = num_path[i-1][j] + num_path[i][j-1]
        for i in range(1, m):
            for j in range(1, n):
                line_path_cnt[j] += line_path_cnt[j - 1]
        return line_path_cnt[-1]

    # dynamic program
    # time overflow
    def uniquePathsDP(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        return self.uniquePathsDP(m-1, n) + self.uniquePathsDP(m, n-1)

    def genSample(self):
        random.seed = (time.time() * 1000) % 131071
        m = random.randint(1, 50)
        n = random.randint(1, 45)
        return m, n