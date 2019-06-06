#coding=utf-8
"""
    Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

    Return the quotient after dividing dividend by divisor.

    The integer division should truncate toward zero.

    Example 1:

    Input: dividend = 10, divisor = 3
    Output: 3

    Example 2:

    Input: dividend = 7, divisor = -3
    Output: -2

    Note:

        Both dividend and divisor will be 32-bit signed integers.
        The divisor will never be 0.
        Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-231,  231 - 1]. For the purpose of this problem, assume that your function returns 231 - 1 when the division result overflows.


"""

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if divisor == 0:
            return False
        if dividend == 0:
            return 0
        a = abs(dividend)
        b = abs(divisor)
        res = 0
        summ = 0
        count = 0
        while a>=b:
            count = 1
            summ = b
            while summ+summ<a:
                summ += summ
                count += count
            a -= summ
            res += count
        if (divisor>0 and dividend>0) or (divisor<0 and dividend<0):
            pass 
        else:
            res = 0-res
        if res > 2**31-1 or res < -2**31:
            return 2**31-1
        else:
            return res


s = Solution()
dividend = 10 
divisor = 3
print s.divide(dividend, divisor)
