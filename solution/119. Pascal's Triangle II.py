# -*- coding: utf-8 -*-
# @Time    : 2020/3/1 21:57
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 119. Pascal's Triangle II.py

from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if 0 <= rowIndex <= 33:
            c = []
            c.append(1)
            if rowIndex == 0:
                return c
            for i in range(1, rowIndex + 1):
                c2 = []
                for j in range(i + 1):
                    if 1 <= j < i:
                        c2.append(c[i - 1][j - 1] + c[i - 1][j])
                    else:
                        c2.append(1)
                c.append(c2)
            return c[rowIndex]
        else:
            return 0


print(Solution().getRow(0))
