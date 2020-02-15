# -*- coding: utf-8 -*-
# @Time    : 2020/2/11 23:09
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 70. Climbing Stairs（大神做法）.py

class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0, 1]
        for i in range(n):
            dp[i % 2] = dp[i % 2] + dp[(i + 1) % 2]

        return dp[(n + 1) % 2]


print(Solution().climbStairs(11))
