class Solution:
# Time: m*n
# Space: m*n
# dp[n][m] means if s[:m] matchs p[:n]
    def isMatch(self, s: str, p: str) -> bool:
        t = [i for i in ('#'+p+'#').split('*') if i!='']
        p = '*'.join(t)[1:-1]
        m, n = len(s), len(p)
        dp = [[True] + [False]*m]
        for i in range(n):
            dp.append([False]*(m+1))
        for i in range(1, n+1):
            dp[i][0] = dp[i-1][0] and p[i-1]=='*'
            for j in range(1,m+1):
                if p[i-1]=='*':
                    dp[i][j] = dp[i-1][j] or (True in dp[i][:j])
                if p[i-1]=='?' or p[i-1]==s[j-1]:
                    dp[i][j] = dp[i-1][j-1]
        return dp[-1][-1]
# Space: n
# 每次动态更新dp的值
    def isMatch(self, s: str, p: str) -> bool:
        t = [i for i in ('#'+p+'#').split('*') if i!='']
        p = '*'.join(t)[1:-1]
        m = len(s)
        dp = [True] + [False]*m
        for i in p:
            if i != '*':
                for j in reversed(range(m)):
                    dp[j+1] = dp[j] and (i == s[j] or i == '?')
            else:
                for j in range(1, m+1):
                    dp[j] = dp[j] or dp[j-1]
            dp[0] = dp[0] and i == '*'
        return dp[-1]
