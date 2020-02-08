# -*- coding: utf-8 -*-
# @Time    : 2020/2/8 17:04
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    :
# @File    : 66.PLus one.py

from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        res = 0
        for count, i in enumerate(reversed(digits)):  # 第一步，把列表转化成整数
            res += i * (10 ** count)
        result = res + 1  # 第二步，对生成的整数进行 +1 运算
        b = [int(x) for x in str(result)]  # 第三步，转化成列表—————采用列表生成式的方法
        return b


print(Solution().plusOne([1, 2, 2, 9]))
