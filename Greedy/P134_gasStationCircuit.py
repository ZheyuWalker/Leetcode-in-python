# There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
#
# You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next
# (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.
#
# Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
# once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        delta = [gas[i] - cost[i] for i in range(n)]

        i = 0
        while i < n:
            if delta[i] >= 0:
                cnt = 0
                stock = 0
                while cnt < n and stock >= 0:
                    stock += delta[(i + cnt) % n]
                    cnt += 1
                if stock >= 0:
                    return i
                else:
                    i += cnt
            else:
                i += 1

        return -1

if __name__ == '__main__':
    gas = [5, 8, 2, 8]
    cost = [6, 5, 6, 6]

    res = Solution().canCompleteCircuit(gas, cost)

    print(res)
