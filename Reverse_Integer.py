#coding=utf-8
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if (x < -2**31) or (x > 2**31-1):
            return 0
            
        if not isinstance(x, int):
            return 0

        fromstr = '%s' %x
        length = len(fromstr)
        if '-' in fromstr:
            tostr = ''.join(fromstr[length-1:0:-1])
            tostr = '-%s' %tostr
        else:
            tostr = ''.join(fromstr[length-1::-1])
        res = int(tostr)
        if (res < -2**31) or (res > 2**31-1):
            return 0
        else:
            return res



s = Solution()
r = s.reverse(1534236469)
print r
