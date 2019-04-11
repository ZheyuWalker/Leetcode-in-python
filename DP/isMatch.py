class Solution:
#backtracking
    def isMatch(self, s: str, p: str) -> bool:
        if not p:
            return not s
        if p[-1] == '*':
            if self.isMatch(s, p[:-2]):
                return True
            if s and (s[-1]==p[-2] or p[-2]=='.'):
                return self.isMatch(s[:-1], p)
        if s and (s[-1]==p[-1] or p[-1]=='.'):
            return self.isMatch(s[:-1], p[:-1])
        return False
#DP
