#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: sortedSquares_977.py
#Author: luhan 
#Created Time: 2019-06-18 11:10:52
############################
"""
Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.

 

Example 1:

Input: [-4,-1,0,3,10]
Output: [0,1,9,16,100]

Example 2:

Input: [-7,-3,2,3,11]
Output: [4,9,9,49,121]

 

Note:

    1 <= A.length <= 10000
    -10000 <= A[i] <= 10000
    A is sorted in non-decreasing order.

"""

class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        return sorted([i**2 for i in A])
        

s = Solution()
A = [-7,-3,2,3,11]
print s.sortedSquares(A)

