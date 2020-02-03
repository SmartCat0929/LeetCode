# -*- coding: utf-8 -*-
# @Time    : 2020/2/2 12:23
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    :
# @File    : 26. Remove Duplicates from Sorted Array

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        lens = len(nums)
        if lens > 0:
            j = 0
            for i in range(lens):
                if nums[j] != nums[i]:
                    j = j + 1
                    nums[j] = nums[i]
            nums= nums[0:(j + 1)]
            return j+1
print(Solution().removeDuplicates([1,2,2,3,3,5,5,5]))
