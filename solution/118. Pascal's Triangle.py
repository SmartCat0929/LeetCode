# -*- coding: utf-8 -*-
# @Time    : 2020/2/29 21:03
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 118. Pascal's Triangle.py
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        c = []
        if numRows == 0:
            return c
        c.append([1])
        if numRows == 1:
            return c
        for i in range(1, numRows):
            c2 = []
            for j in range(i + 1):
                if 1 <= j < i:
                    c2.append(c[i - 1][j - 1] + c[i - 1][j])
                else:
                    c2.append(1)
            c.append(c2)
        return c


print(Solution().generate(5))
