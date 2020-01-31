# -*- coding: utf-8 -*-
# @Time    : 2020/1/30 19:14
# @Author  : SmartCat0929
# @Email   : 1027699719@qq.com
# @Link    : https://github.com/SmartCat0929
# @Site    : 
# @File    : 12. Integer to Roman(自己想的复杂的算法）.py

class Solution:
    def intToRoman(self, num: int) -> str:
        numStr = str(num)
        if num < 10:
            if int(numStr[-1]) > 0 and int(numStr[-1]) < 4:
                units = ""
                for i in range(0, int(numStr[-1])):
                    units = "I" + units
            elif int(numStr[-1]) == 4:
                units = "IV"
            elif int(numStr[-1]) == 5:
                units = "V"
            elif int(numStr[-1]) > 5 and int(numStr[-1]) < 9:
                units = "V"
                for i in range(5, int(numStr[-1])):
                    units = units + "I"
            elif int(numStr[-1]) == 9:
                units = "IX"
            return units
        elif num >= 10 and num <= 99:  # 如果是两位数
            if int(numStr[-1]) == 0:
                units = ""
            elif int(numStr[-1]) > 0 and int(numStr[-1]) < 4:  # 个位
                units = ""
                for i in range(0, int(numStr[-1])):
                    units = "I" + units
            elif int(numStr[-1]) == 4:
                units = "IV"
            elif int(numStr[-1]) == 5:
                units = "V"
            elif int(numStr[-1]) > 5 and int(numStr[-1]) < 9:
                units = "V"
                for i in range(5, int(numStr[-1])):
                    units = units + "I"
            elif int(numStr[-1]) == 9:
                units = "IX"
            if int(numStr[-2]) == 1:  # 十位
                decades = "X"
            elif int(numStr[-2]) > 0 and int(numStr[-2]) < 4:  # 十位
                decades = ""
                for j in range(0, int(numStr[-2])):
                    decades = "X" + decades
            elif int(numStr[-2]) == 4:
                decades = "XL"
            elif int(numStr[-2]) == 5:
                decades = "L"
            elif int(numStr[-2]) > 5 and int(numStr[-2]) < 9:
                decades = "L"
                for j in range(5, int(numStr[-2])):
                    decades = decades + "X"
            elif int(numStr[-2]) == 9:
                decades = "XC"
            romans = decades + units
            return romans

        elif num >= 100 and num <= 999:  # 如果是三位数
            if int(numStr[-1]) == 0:  # 个位
                units = ""
            elif int(numStr[-1]) > 0 and int(numStr[-1]) < 4:
                units = ""
                for i in range(0, int(numStr[-1])):
                    units = "I" + units
            elif int(numStr[-1]) == 4:
                units = "IV"
            elif int(numStr[-1]) == 5:
                units = "V"
            elif int(numStr[-1]) > 5 and int(numStr[-1]) < 9:
                units = "V"
                for i in range(5, int(numStr[-1])):
                    units = units + "I"
            elif int(numStr[-1]) == 9:
                units = "IX"
            if int(numStr[-2]) == 0:  # 十位
                decades = ""
            elif int(numStr[-2]) > 0 and int(numStr[-2]) < 4:
                decades = ""
                for j in range(0, int(numStr[-2])):
                    decades = "X" + decades
            elif int(numStr[-2]) == 4:
                decades = "XL"
            elif int(numStr[-2]) == 5:
                decades = "L"
            elif int(numStr[-2]) > 5 and int(numStr[-2]) < 9:
                decades = "L"
                for j in range(5, int(numStr[-2])):
                    decades = decades + "X"
            elif int(numStr[-2]) == 9:
                decades = "XC"
            if int(numStr[-3]) > 0 and int(numStr[-3]) < 4:  # 百位
                hundreds = ""
                for j in range(0, int(numStr[-3])):
                    hundreds = "C" + hundreds
            elif int(numStr[-3]) == 4:
                hundreds = "CD"
            elif int(numStr[-3]) == 5:
                hundreds = "D"
            elif int(numStr[-3]) > 5 and int(numStr[-3]) < 9:
                hundreds = "D"
                for j in range(5, int(numStr[-3])):
                    hundreds = hundreds + "C"
            elif int(numStr[-3]) == 9:
                hundreds = "CM"
            romans = hundreds + decades + units
            return romans

        elif num >= 1000 and num <= 3999:  # 如果是四位数
            if int(numStr[-1]) == 0:  # 个位
                units = ""
            elif int(numStr[-1]) > 0 and int(numStr[-1]) < 4:
                units = ""
                for i in range(0, int(numStr[-1])):
                    units = "I" + units
            elif int(numStr[-1]) == 4:
                units = "IV"
            elif int(numStr[-1]) == 5:
                units = "V"
            elif int(numStr[-1]) > 5 and int(numStr[-1]) < 9:
                units = "V"
                for i in range(5, int(numStr[-1])):
                    units = units + "I"
            elif int(numStr[-1]) == 9:
                units = "IX"
            if int(numStr[-2]) == 0:  # 十位
                decades = ""
            elif int(numStr[-2]) > 0 and int(numStr[-2]) < 4:
                decades = ""
                for j in range(0, int(numStr[-2])):
                    decades = "X" + decades
            elif int(numStr[-2]) == 4:
                decades = "XL"
            elif int(numStr[-2]) == 5:
                decades = "L"
            elif int(numStr[-2]) > 5 and int(numStr[-2]) < 9:
                decades = "L"
                for j in range(5, int(numStr[-2])):
                    decades = decades + "X"
            elif int(numStr[-2]) == 9:
                decades = "XC"
            if int(numStr[-3]) == 0:  # 百位
                hundreds = ""
            elif int(numStr[-3]) > 0 and int(numStr[-3]) < 4:
                hundreds = ""
                for j in range(0, int(numStr[-3])):
                    hundreds = "C" + hundreds
            elif int(numStr[-3]) == 4:
                hundreds = "CD"
            elif int(numStr[-3]) == 5:
                hundreds = "D"
            elif int(numStr[-3]) > 5 and int(numStr[-3]) < 9:
                hundreds = "D"
                for j in range(5, int(numStr[-3])):
                    hundreds = hundreds + "C"
            elif int(numStr[-3]) == 9:
                hundreds = "CM"
            if int(numStr[-4]) > 0 and int(numStr[-4]) < 4: #千位
                thousands = ""
                for j in range(0, int(numStr[-4])):
                    thousands = "M" + thousands
                romans = thousands + hundreds + decades + units
                return romans
        elif num > 3999:
            return 0


print(Solution().intToRoman(400))
