# -*- coding: utf-8 -*-
# @Time    : 2020/3/12 22:14
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 125. Valid Palindrome.py


class Solution:
    def isPalindrome(self, s: str) -> bool:
        temp0 = s.lower()
        temp = filter(str.isalnum, temp0)
        print(temp)
        print(*temp)
        s = [*temp]
        return s == s[::-1]


print(Solution().isPalindrome("A man, a plan, a canal: Panama"))
