# -*- coding: utf-8 -*-
# @Time    : 2020/2/16 14:03
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 70. Climbing Stairs.py


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        count1, count2 = (1, 2)
        for i in range(2, n):
            count = count1 + count2
            count1 = count2
            count2 = count
        return count


print(Solution().climbStairs(11))
