#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: toLowerCase_709.py
#Author: luhan 
#Created Time: 2019-06-06 11:13:09
############################


"""
    Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.

     

    Example 1:

    Input: "Hello"
    Output: "hello"

    Example 2:

    Input: "here"
    Output: "here"

    Example 3:

    Input: "LOVELY"
    Output: "lovely"


"""

class Solution(object):
    def toLowerCase(self, strr):
        """
        :type str: strr
        :rtype: strr
        """
        s = ''
        for char in strr:
            asci = ord(char)
            if asci>=ord('A') and asci<=ord('Z'):
                s += chr(asci+32)
            else:
                s += char
        return s

s = Solution()
str = 'LOVELY'
print s.toLowerCase(str)
