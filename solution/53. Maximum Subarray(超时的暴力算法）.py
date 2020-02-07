# -*- coding: utf-8 -*-
# @Time    : 2020/2/6 22:15
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 53. Maximum Subarray(超时的暴力算法）.py
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = -9999999999
        if len(nums)>1:
            maxSum = -99999
            for i in range(0, len(nums)):
                for j in range(i, len(nums)):
                    thisSum = sum(nums[i:j+1])
                    if thisSum > maxSum:
                        maxSum = thisSum
            return maxSum
        elif len(nums)==1:
            maxSum=nums[0]
            return maxSum
        else:
            return 0

print(Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
