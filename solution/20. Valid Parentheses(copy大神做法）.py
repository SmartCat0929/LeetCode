# -*- coding: utf-8 -*-
# @Time    : 2020/1/31 10:37
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 20. Valid Parentheses(copy大神做法）.py

class Solution:
    def isValid(self, s: str) -> bool:
            bracket_map = {"(": ")", "[": "]", "{": "}"}
            open_par = set(["(", "[", "{"])
            stack = []
            for i in s:
                if i in open_par:
                    stack.append(i)
                elif stack and i == bracket_map[stack[-1]]:
                    stack.pop()
                else:
                    return False
            return stack == []
print(Solution().isValid("{[[(])]}"))

