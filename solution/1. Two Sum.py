# -*- coding: utf-8 -*-
# @Time    : 2020/1/25 21:01
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 1. Two Sum.py

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, n in enumerate(nums):
            if d.get(n) is None:
                d[n] = i

            r = target - n
            j = d.get(r)
            if j is not None and j != i:
                return [i, j]


print(Solution().twoSum([3, 3], 6))
