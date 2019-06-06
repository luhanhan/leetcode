#coding=utf-8
class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x==0:
            return True
        if x<0: 
            return False
            
        count = self.cal_count(x)
        while x:
            fn = x//(10**count)
            ln = x%10
            if fn!=ln:
                return False
            x = x % (10**count)/ 10
            count = count-2  
        return True                                                                                                                                                                                          
    


    def cal_count(self, x): 
        count = 0 
        while x:
            count += 1
            x = x//10
        return count-1


s = Solution()
print s.isPalindrome(1000021)
