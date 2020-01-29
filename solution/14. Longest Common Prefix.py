# -*- coding: utf-8 -*-
# @Time    : 2020/1/29 12:28
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 14. Longest Common Prefix.py

from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        d = len(strs)
        minLength = 999999
        for str in strs:
            thisLength = len(str)
            if thisLength < minLength:
                minLength = thisLength
        res = ""
        if d > 0:
            for i in range(minLength):
                n = 0
                r = strs[0][i]
                for j in range(d):
                    if r == strs[j][i]:
                        n = n + 1
                        if n == d:
                            break
                    else:
                        return res
                res = res + r
            return res
        else:
            return res


# print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
print(Solution().longestCommonPrefix([""]))

