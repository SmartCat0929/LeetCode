# -*- coding: utf-8 -*-
# @Time    : 2020/3/14 23:09
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 136. Single Number.py
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # 亦或运算
        a = 0
        for i in nums:
            a ^= i
        return a


print(Solution().singleNumber([7, 1, 1, 7, 6, 5, 6]))
