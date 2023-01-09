# Given two strings text1 and text2, return the length of their longest common subsequence.
# If there is no common subsequence, return 0.
#
# A subsequence of a string is a new string generated from the original string with some characters (can be none)
# deleted without changing the relative order of the remaining characters.
#
# For example, "ace" is a subsequence of "abcde".
# A common subsequence of two strings is a subsequence that is common to both strings.


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        if m == 0 or n == 0:
            return 0

        seq = [[0 for j in range(n+1)] for i in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    seq[i+1][j+1] = 1 + seq[i][j]
                else:
                    seq[i+1][j+1] = max(seq[i][j+1], seq[i+1][j])
        return seq[m][n]
