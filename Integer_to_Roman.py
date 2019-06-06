#coding=utf-8
"""

Given an integer, convert it to a roman numeral. Input is guaranteed to be within the range from 1 to 3999.

Example 1:
Input: 3
Output: "III"

Example 2:
Input: 4
Output: "IV"

Example 3:
Input: 9
Output: "IX"

Example 4:
Input: 58
Output: "LVIII"
Explanation: C = 100, L = 50, XXX = 30 and III = 3.

Example 5:
Input: 1994
Output: "MCMXCIV"
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str

        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """

        romandict = {'1':'I', '5':'V', '10':'X', '50':'L', '100':'C', '500':'D', '1000':'M'}
        countroman = {'4': 'IV', '9':'IX', '40':'XL', '90':'XC', '400':'CD', '900':'CM'}
        resroman = ''
        if num < 1 or num > 3999:
            return None
        
        _tmp = num
        count = -1 
        while _tmp:
            count += 1
            _tmp = _tmp//10

        romanlist = []
        while num:
            f = num/(10**count)
            if f>=5 and f<9:
                ff = f-5
                romanlist.append(str(10**count*5))
                _tmp = [str(10**count)] * ff
                if _tmp:
                    romanlist.extend(_tmp)
            elif f>=1 and f<4:
                ff = f
                _tmp = [str(10**count)] * ff
                if _tmp:
                    romanlist.extend(_tmp)
            elif f!=0:
                romanlist.append(str(10**count*f))
            else:
                pass
            num = num%(10**count)
            count -= 1
        print romanlist
        for f in romanlist:
            if f in countroman:
                resroman += countroman[f]
            else:
                resroman += romandict[f]
        return resroman

s = Solution()
data = [3, 4, 9, 58, 1994, 101]
#data = [3, 4]
for d in data:
    print s.intToRoman(d)

#Output: "III"
#
#Output: "IV"
#
#Output: "IX"
#
#Input: 58
#Output: "LVIII"
#
#Input: 1994
#Output: "MCMXCIV"
