# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 12:21
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 13. Roman to Integer.py

class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        y = 0
        d = []
        for j in (s):
            d.append(j)
        for i in range(l):
            if d[i]=="V"and d[i-1]=="I"and i!=0:
                y=y+3
            elif d[i]=="X"and d[i-1]=="I"and i!=0:
                y=y+8
            elif d[i]=="L"and d[i-1]=="X"and i!=0:
                y=y+30
            elif d[i]=="C"and d[i-1]=="X"and i!=0:
                y=y+80
            elif d[i]=="D"and d[i-1]=="C"and i!=0:
                y=y+300
            elif d[i]=="M"and d[i-1]=="C"and i!=0:
                y=y+800
            elif d[i] == "I":
                y = y + 1
            elif d[i] == "V":
                y = y + 5
            elif d[i] == "X":
                y = y + 10
            elif d[i]== "L":
                y = y + 50
            elif d[i] == "C":
                y = y + 100
            elif d[i] == "D":
                y = y + 500
            elif d[i] == "M":
                y = y + 1000
        if y>=1 and y<=3999:
            return y
        else:
            return 0

print (Solution().romanToInt("MMMCDXC"))