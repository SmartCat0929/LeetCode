# -*- coding: utf-8 -*-
# @Time    : 2020/1/26 12:33
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    :
# @File    : 7. Reverse Integer.py

class Solution:
    def reverse(self, x: int) -> int:
        if x >= -2147483648 and x <= 2147483647:
            if x >= 0:
                r = ""
            else:
                r = "-"
            w = abs(x)
            y = str(w)
            n = len(y)
            d = []
            for i in (y):
                d.append(i)
            for j in range(n):
                c = d.pop()
                r = r + c
                v = int(r)
            if v >= -2147483648 and v <= 2147483647:
                return v
            else:
                return 0
        else:
            return 0


print(Solution().reverse(12422))
