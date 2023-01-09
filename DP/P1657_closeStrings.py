# Two strings are considered close if you can attain one from the other using the following operations:
#
# Operation 1: Swap any two existing characters.
# For example, abcde -> aecdb
# Operation 2: Transform every occurrence of one existing character into another existing character, and do the same with the other character.
# For example, aacabb -> bbcbaa (all a's turn into b's, and all b's turn into a's)
# You can use the operations on either Hash as many times as necessary.
#
# Given two strings, word1 and word2, return true if word1 and word2 are close, and false otherwise.


class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        def cnt_alpha(s):
            d = dict()
            for i in range(ord('a'), ord('z') + 1):
                n = s.count(chr(i))
                if n in d:
                    d[n].append(chr(i))
                else:
                    d[n] = [chr(i)]
            return d

        if len(word1) != len(word2):
            return False
        for c in word2:
            if c not in word1:
                return False

        d1 = cnt_alpha(word1)
        d2 = cnt_alpha(word2)

        if len(d1) != len(d2):
            return False

        for k in d1.keys():
            if k not in d2:
                return False
            if len(d1[k]) != len(d2[k]):
                return False

        return True