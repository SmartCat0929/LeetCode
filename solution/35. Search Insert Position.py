# -*- coding: utf-8 -*-
# @Time    : 2020/2/4 16:33
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 35. Search Insert Position.py
from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        lens=len(nums)
        if target in nums:
            return nums.index(target)
        else:
            if target < nums[-1]:
                for i in range(lens):
                    if target < nums[i]:
                        nums.insert(i,target)
                        return nums.index(target)
            else:
                return lens
print(Solution().searchInsert([1,4,5,6,9],10))