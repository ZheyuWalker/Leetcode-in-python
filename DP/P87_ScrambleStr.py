# We can scramble a Hash s to get a Hash t using the following algorithm:
# If the length of the Hash is 1, stop. If the length of the Hash is > 1, do the following:
# 1. Split the Hash into two non-empty substrings at a random index, i.e., if the Hash is s, divide it to x and y
# where s = x + y.
# 2. Randomly decide to swap the two substrings or to keep them in the same order. i.e., after this step, s may become
# s = x + y or s = y + x.
# 3. Apply step 1 recursively on each of the two substrings x and y.
# Given two strings s1 and s2 of the same length, return true if s2 is a scrambled Hash of s1,
# otherwise, return false.
from functools import lru_cache


class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        def equal_char(s1, s2):
            return sorted(s1) == sorted(s2)

        @lru_cache(maxsize=None)
        def isScramble_(s1, s2):
            if s1 == s2:
                return True

            n = len(s1)
            if not equal_char(s1, s2):
                return False

            for i in range(1, n):
                if isScramble_(s1[:i], s2[:i]) and isScramble_(s1[i:], s2[i:]):
                    return True
                if isScramble_(s1[:i], s2[n-i:n]) and isScramble_(s1[i:], s2[:n-i]):
                    return True
            return False

        return isScramble_(s1, s2)


if __name__ == '__main__':
    s1 = 'great'
    s2 = 'rgeat'
    print(Solution().isScramble(s1, s2))

