class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) == 1:
            return int(tokens[0])
        nums = []
        ops = {'+', '-', '*', '/'}
        for c in tokens:
            if c not in ops:
                nums.append(c)
            else:
                n2 = nums.pop()
                n1 = nums.pop()
                if c != '/':
                    nums.append(str(eval(''.join([n1, c, n2]))))
                else:
                    n1, n2 = int(n1), int(n2)
                    if n1 < 0 or n2 < 0:
                        nums.append(str(-(abs(n1) // abs(n2))))
                    else:
                        nums.append(str(n1 // n2))


        return int(nums[-1])


if __name__ == '__main__':
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(Solution().evalRPN(tokens))
