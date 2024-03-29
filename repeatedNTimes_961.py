#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: repeatedNTimes_961.py
#Author: luhan 
#Created Time: 2019-06-17 15:43:20
############################
"""
In a array A of size 2N, there are N+1 unique elements, and exactly one of these elements is repeated N times.

Return the element repeated N times.

 

Example 1:

Input: [1,2,3,3]
Output: 3

Example 2:

Input: [2,1,2,5,3,2]
Output: 2

Example 3:

Input: [5,1,5,2,5,3,5,4]
Output: 5

 

Note:

    4 <= A.length <= 10000
    0 <= A[i] < 10000
    A.length is even

"""

class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        #return int((sum(A)-sum(set(A))) // (len(A)//2-1))
        import collections
        count = collections.Counter(A)
        for k in count:
            if count[k] > 1:
                return k


s = Solution()
A = [2,1,2,5,3,2]
print s.repeatedNTimes(A)
