# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 11:33
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 12. Integer to Roman（聪明的做法）.py


class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        s = 1000

        d = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
        while num != 0:
            r, temp = divmod(num, s)

            if r == 9:
                res += d[s] + d[s * 10]
            elif r == 4:
                res += d[s] + d[s * 5]
            elif r >= 5:
                res += d[s * 5] + d[s] * (r - 5)
            else:
                res += d[s] * r

            s = s // 10
            num = temp

        return res


print(Solution().intToRoman(2964))
