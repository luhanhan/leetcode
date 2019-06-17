#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: sortArrayByParity_905.py
#Author: luhan 
#Created Time: 2019-06-17 15:22:20
############################
"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

You may return any answer array that satisfies this condition.

 

Example 1:

Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

 

Note:

    1 <= A.length <= 5000
    0 <= A[i] <= 5000

"""

class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        res = []
        for i in A:
            if i%2==0:
                res.insert(0,i)
            else:
                res.append(i)
        return res
        

s = Solution()
A = [3,1,2,4]
print s.sortArrayByParity(A)
