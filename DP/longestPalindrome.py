class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        i = 0
        rlt = s[0]
        for i in range(n-1):
            r = i+1
            while r<n and s[i] == s[r]:
                r+=1
            temp = s[i:r]
            l = i-1
            while l>=0 and r<n:
                if s[l] != s[r]:
                    break
                temp = s[l]+temp+s[r]
                l,r = l-1, r+1
            rlt = temp if len(temp)>len(rlt) else rlt
        return rlt
  
      def longestPalindrome_Manacher(self, s: str) -> str:
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$".
        # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range (1, n-1):
            P[i] = (R > i) and min(R - i, P[2*C - i]) # equals to i' = C - (i-C)
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1
    
            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]
    
        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return s[(centerIndex  - maxLen)//2: (centerIndex  + maxLen)//2]
