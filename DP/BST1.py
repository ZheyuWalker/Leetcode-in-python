class Solution:
    def numTrees(self, n: int) -> int:
        dp = [1] + [0 for _ in range(n)]
        for i in range(1, n+1):
            for j in range(i):
                # 以(j+1)为树根时，左子树右子树分别有dp[j]/dp[i-1-j]种可能
                dp[i] += dp[j]*dp[i-1-j]
        return dp[-1]
