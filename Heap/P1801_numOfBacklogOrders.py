# You are given a 2D integer array orders, where each orders[i] = [pricei, amounti, orderTypei] denotes that amounti
# orders have been placed of type orderTypei at the price pricei. The orderTypei is:
# 0 if it is a batch of buy orders, or
# 1 if it is a batch of sell orders.
# Note that orders[i] represents a batch of amounti independent orders with the same price and order type.
# All orders represented by orders[i] will be placed before all orders represented by orders[i+1] for all valid i.
#
# There is a backlog that consists of orders that have not been executed. The backlog is initially empty.
# When an order is placed, the following happens:
#
# If the order is a buy order, you look at the sell order with the smallest price in the backlog.
# If that sell order's price is smaller than or equal to the current buy order's price, they will match and be executed,
# and that sell order will be removed from the backlog. Else, the buy order is added to the backlog.
# Vice versa, if the order is a sell order, you look at the buy order with the largest price in the backlog.
# If that buy order's price is larger than or equal to the current sell order's price, they will match and be executed,
# and that buy order will be removed from the backlog. Else, the sell order is added to the backlog.
# Return the total amount of orders in the backlog after placing all the orders from the input.
# Since this number can be large, return it modulo 10**9 + 7.
from typing import List
from heapq import *


class Solution:
    def getNumberOfBacklogOrders(self, orders: List[List[int]]) -> int:

        buy_heap = []
        sell_heap = []

        for order in orders:
            cnt = order[1]
            if order[2] == 0:
                while sell_heap and cnt > 0:
                    sell_log = heappop(sell_heap)
                    if sell_log[0] <= order[0]:
                        cnt -= sell_log[1]
                        if cnt < 0:
                            heappush(sell_heap, (sell_log[0], -cnt))
                    else:
                        heappush(sell_heap, sell_log)
                        break
                if cnt > 0:
                    heappush(buy_heap, (-order[0], cnt))

            else:
                while buy_heap and cnt > 0:
                    buy_log = heappop(buy_heap)
                    if -buy_log[0] >= order[0]:
                        cnt -= buy_log[1]
                        if cnt < 0:
                            heappush(buy_heap, (buy_log[0], -cnt))
                    else:
                        heappush(buy_heap, buy_log)
                        break
                if cnt > 0:
                    heappush(sell_heap, (order[0], cnt))

        backlog = 0
        for order in sell_heap + buy_heap:
            backlog = (backlog + order[1]) % (10 ** 9 + 7)

        return backlog


if __name__ == '__main__':
    orders = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
    res = Solution().getNumberOfBacklogOrders(orders)
    print(res)
