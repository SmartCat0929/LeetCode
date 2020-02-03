# -*- coding: utf-8 -*-
# @Time    : 2020/2/3 15:38
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 27. Remove Element.py
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        lens = len(nums)
        if lens > 0: #判断列表是否为空
            j = 0
            for i in range(lens):
                if nums[i] != val: #若i指定的数字不等于val
                    temp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = temp  #i和j指向的数字位置互换
                    j = j + 1 #j再往后移动
            return j
print(Solution().removeElement([3,3,2],3))
