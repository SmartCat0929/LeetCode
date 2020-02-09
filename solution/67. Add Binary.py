# -*- coding: utf-8 -*-
# @Time    : 2020/2/9 11:18
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 67. Add Binary.py


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a1 = "0b" + a
        b1 = "0b" + b
        sum1 = int(a1, 2) + int(b1, 2)  # 第一步 转换成十进制后的简单相加
        sum2 = bin(sum1)  # 第二步 将相加后的和转换成二进制
        a = [x for x in sum2]  # 第三步 bin方法转换后的二进制有0b前缀，用列表生成式将他转换成列表
        b = a[2:]  # 第四步 采用切片，去除前两位前缀
        sum3 = ''.join(b)  # 第五步 采用join方法将列表内部元素合并
        return sum3


print(Solution().addBinary("1010", "1011"))
