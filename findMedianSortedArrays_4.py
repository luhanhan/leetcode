#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: findMedianSortedArrays_4.py
#Author: luhan 
#Created Time: 2019-06-27 16:00:28
############################

"""
There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0

Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5


"""

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


s = Solution()
nums1 = [1,2]
nums2 = [3,4]
print s.findMedianSortedArrays(nums1, nums2)
