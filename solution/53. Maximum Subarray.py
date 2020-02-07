# -*- coding: utf-8 -*-
# @Time    : 2020/2/7 16:12
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 53. Maximum Subarray.py

from typing import List
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        tmp = 0
        res = float('-inf')
        for i in range(n):
            if tmp < 0:
                tmp = 0
            tmp = tmp + nums[i]
            res = max(res, tmp)
        return res
print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))