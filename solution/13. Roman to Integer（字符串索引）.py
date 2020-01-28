# -*- coding: utf-8 -*-
# @Time    : 2020/1/28 14:35
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 13. Roman to Integer（字符串索引）.py

class Solution:
    def romanToInt(self, s: str) -> int:
        l = len(s)
        y = 0
        for i in range(l):
            if s[i]=="V"and s[i-1]=="I"and i!=0:
                y=y+3
            elif s[i]=="X"and s[i-1]=="I"and i!=0:
                y=y+8
            elif s[i]=="L"and s[i-1]=="X"and i!=0:
                y=y+30
            elif s[i]=="C"and s[i-1]=="X"and i!=0:
                y=y+80
            elif s[i]=="D"and s[i-1]=="C"and i!=0:
                y=y+300
            elif s[i]=="M"and s[i-1]=="C"and i!=0:
                y=y+800
            elif s[i] == "I":
                y = y + 1
            elif s[i] == "V":
                y = y + 5
            elif s[i] == "X":
                y = y + 10
            elif s[i]== "L":
                y = y + 50
            elif s[i] == "C":
                y = y + 100
            elif s[i] == "D":
                y = y + 500
            elif s[i] == "M":
                y = y + 1000
        if y>=1 and y<=3999:
            return y
        else:
            return 0

print (Solution().romanToInt("MMMCDXC"))