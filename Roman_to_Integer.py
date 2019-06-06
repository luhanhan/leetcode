#coding=utf-8
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        
        I can be placed before V (5) and X (10) to make 4 and 9. 
        X can be placed before L (50) and C (100) to make 40 and 90. 
        C can be placed before D (500) and M (1000) to make 400 and 900.
        """
        romandict = {'I':1,'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        subdict = {'I':['V','X'], 'X':['L','C'], 'C':['D','M']}
        resint = 0
        flag = False
        for index,i in enumerate(s):
            if flag == True:
                flag = False
                continue
            if index+1<=len(s)-1:
                if (i in subdict) and (s[index+1] in subdict[i]):
                    resint += romandict[s[index+1]] - romandict[s[index]]
                    flag = True
                else:
                    flag = False
                    resint += romandict[s[index]]
            else:
                flag = False
                resint += romandict[s[index]]

        return resint
        
s = Solution()
ss = 'III'
print s.romanToInt(ss)

ss = 'IV'
print s.romanToInt(ss)

ss = 'VI'
print s.romanToInt(ss)

ss = 'IX'
print s.romanToInt(ss)

ss = 'MCMXCIV'
print s.romanToInt(ss)
