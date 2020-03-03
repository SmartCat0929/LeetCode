# -*- coding: utf-8 -*-
# @Time    : 2020/3/3 11:22
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 122. Best Time to Buy and Sell Stock II.py


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lens = len(prices)
        if lens == 0 or lens == 1:
            return 0
        profit = 0
        for i in range(1, lens):
            temp = prices[i] - prices[i - 1]
            if temp > 0:
                profit = profit + temp
        return profit


print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))
