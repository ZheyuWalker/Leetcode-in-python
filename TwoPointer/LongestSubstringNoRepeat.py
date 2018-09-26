class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = rlt = 0
        used = {}
        for i in range(len(s)):
            if s[i] in used and head <= used[s[i]]:
                head = used[s[i]] + 1
            else:
                rlt = max(rlt, i-head+1)
            used[s[i]] = i
        return rlt  

    def lengthOfLongestSubstring_naive(self, s):
        """
        :type s: str
        :rtype: int
        """
        buff = {}
        if len(s) == 0:
            return 0
        rlt = 1
        for i in range(len(s)):
            buff[s[i]] = 1
            j = i+1
            while j < len(s):
                if s[j] in buff:
                    rlt = max(rlt, j-i)
                    buff = {}
                    break
                elif j == len(s)-1:
                    rlt = max(rlt, j-i+1)
                    break
                else:
                    buff[s[j]] = 1
                    j += 1
        return rlt
                    
