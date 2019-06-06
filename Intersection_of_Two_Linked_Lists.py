#coding=utf-8
#!/usr/b:in/env python
# -*- coding: utf-8 -*-
# lh @ 2014-12-15 19:06:50

# https://oj.leetcode.com/problems/intersection-of-two-linked-lists/
# Your code should preferably run in O(n) time and use only O(1) memory.

# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None

        lena = self.getlen(headA)
        lenb = self.getlen(headB)
        if lenb < lena:
            (headA, headB) = (headB, headA)
        delt = lenb - lena

        if delt < 0 : delt = 0-delt

        for i in range(delt):
            headB = headB.next
        while True:
            if headA is None or headB is None:
                return None
            if headA == headB:
                return headA

            headA = headA.next
            headB = headB.next


    def getlen(self, head):
        len = 0
        while head is not None:
            len += 1
            head = head.next
        return len
