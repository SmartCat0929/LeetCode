# -*- coding: utf-8 -*-
# @Time    : 2020/1/27 17:28
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 9. Palindrome Number.py

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x > 0:
            r = 0
            y = str(x)
            n = len(y)
            d = []
            for i in (y):
                d.append(i)
            for j in range(n):
                c = d.pop()
                r = r + c
                v = int(r)
            if v == x:
                return v
            else:
                return 0
        elif x== 0:
            return True
        else:
            return 0


print(Solution().isPalindrome(12321))
