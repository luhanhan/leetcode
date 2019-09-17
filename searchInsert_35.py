#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: searchInsert_35.py
#Author: luhan 
#Created Time: 2019-06-28 15:27:45
############################
"""
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0


"""

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        res = 0
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left+(right-left)/2
            if num(mid) > target:
                right = mid-1
            if num(mid) < target:
                left = mid+1
            if num(mid) == target:
                return mid
        return -1

s = Solution()
nums = [1.3.5.6]
target = 5
