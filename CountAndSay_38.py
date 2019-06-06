#coding=utf-8
"""
    The count-and-say sequence is the sequence of integers with the first five terms as following:

    1.     1
    2.     11
    3.     21
    4.     1211
    5.     111221

    1 is read off as "one 1" or 11.
    11 is read off as "two 1s" or 21.
    21 is read off as "one 2, then one 1" or 1211.

    Given an integer n where 1 =< n >= 30, generate the nth term of the count-and-say sequence.
    Note: Each term of the sequence of integers will be represented as a string.

     

    Example 1:

    Input: 1
    Output: "1"

    Example 2:

    Input: 4
    Output: "1211"

"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n<1 or n>30:
            return 'error'
        if n==1:
            return '1'
        last = self.countAndSay(n-1)
        l = []
        for item in str(last):
            if not l:
                l.append(item)
            else:
                if item == l[-1][0]:
                    l[-1] += item
                else:
                    l.append(item)
        res = ''
        for item in l:
            count, num = len(item), item[0]
            sss = str(count)+str(num)
            res += sss
        return res

s = Solution()
for i in range(8): 
    print i
    print s.countAndSay(i)
    print '=========='
