# Given a pattern and a string s, find if s follows the same pattern.
#
# Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.


class Solution:
    def wordPattern_1(self, pattern: str, s: str) -> bool:
        p = pattern
        t = s.split()
        return map(p.find, p) == map(t.index, t)

    def wordPattern_2(self, pattern: str, s: str) -> bool:
        f = lambda x: map({}.setdefault, x, range(len(x)))
        return f(pattern) == f(s.split())

    def wordPattern_3(self, pattern: str, s: str) -> bool:
        p = pattern
        t = s.split()
        return len(set(zip(p, t))) == len(set(p)) == len(set(t)) and len(s) == len(t)


if __name__ == '__main__':
    pattern = "abba"
    s = "dog cat cat dog"
