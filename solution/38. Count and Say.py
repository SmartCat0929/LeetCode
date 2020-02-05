# -*- coding: utf-8 -*-
# @Time    : 2020/2/5 10:54
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 38. Count and Say.py

class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        elif n == 2:
            return "11"
        string = "11"  #在11的基础上开始变换
        for i in range(2, n):
            newsb = []        #设立一个空列表
            prev = string[0]  #记住第一个字符
            cnt = 1
            for symbol in string[1:]:
                if symbol == prev:
                    cnt += 1            # 通过循环，记住第一个字符重复的次数
                else:
                    newsb.append(str(cnt) + prev)   #若后续字符与第一个字符不重复，返回 1个”第一个字符“
                    prev = symbol  #  改为记住后续字符
                    cnt = 1  # 默认该字符出现次数为1
            newsb.append(str(cnt) + prev)   #若后续字符与第一个字符重复，返回 几个”第一个字符“
            string = "".join(newsb)
        return string
print(Solution().countAndSay(4))