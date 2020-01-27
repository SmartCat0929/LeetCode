# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 19:09
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 7. Reverse Integer（底层做法）.py

class Solution:
    def reverse(self, x: int) -> int:
        if x >= -2147483648 and x <= 2147483647:
            c = 0
            if x >= 0:
                while x != 0:
                    c = c * 10 + x % 10
                    x = x // 10
            else:
                y = 0 - x
                while y != 0:
                    c = c * 10 + y % 10
                    y = y // 10
                c = 0 - c
            if c >= -2147483648 and c <= 2147483647:
                return c
            else:
                return 0
        else:
            return 0


print(Solution().reverse(-120))
