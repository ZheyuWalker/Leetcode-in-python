# It is a sweltering summer day, and a boy wants to buy some ice cream bars.
#
# At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of
# the ith ice cream bar in coins.
# The boy initially has coins to spend, and he wants to buy as many icecream bars as possible.
#
# Return the maximum number of ice cream bars the boy can buy with coins.
#
# Note: The boy can buy the ice cream bars in any order.


from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = len(costs)

        if coins < costs[0]:
            return 0

        for i in range(1, len(costs)):
            costs[i] += costs[i-1]
            if coins < costs[i]:
                return i

        return n


if __name__ == '__main__':
    costs = [1, 6, 3, 1, 2, 5]
    coins = 20

    res = Solution().maxIceCream(costs, coins)

    print(res)
