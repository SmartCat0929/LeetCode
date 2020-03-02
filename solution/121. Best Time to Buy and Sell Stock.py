# -*- coding: utf-8 -*-
# @Time    : 2020/3/2 13:33
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 121. Best Time to Buy and Sell Stock.py
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lens = len(prices)

        if lens == 0 or lens == 1:
            return 0

        min_price = prices[0]
        profit = 0
        for i in range(1, lens):
            if prices[i] < min_price:
                min_price = prices[i]
            if prices[i] - min_price > profit:
                profit = prices[i] - min_price
        return profit


print(Solution().maxProfit([2, 4, 1]))
