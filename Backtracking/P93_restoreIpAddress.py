from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        def ip_address(idx, part):
            nonlocal s
            if len(s) - idx < part - 1 or len(s) - idx > 3 * part:
                return []
            if part == 1:
                return [] if int(s[idx:]) > 255 or (len(s[idx:]) >= 2 and s[idx] == '0') else [s[idx:]]

            res = []
            for i in range(1, min(4, len(s) - idx)):
                if i >= 2 and (int(s[idx:idx + i]) > 255 or s[idx] == '0'):
                    continue
                res += ['.'.join([s[idx:idx + i], _]) for _ in ip_address(idx + i, part - 1)]
            return res

        return ip_address(0, 4)


if __name__ == '__main__':
    # s = "0000"
    # s = "25525511135"
    s = "101023"
    res = Solution().restoreIpAddresses(s)
    print(res)
