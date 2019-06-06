#coding=utf-8
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = self.transform2num(l1)
        num2 = self.transform2num(l2)
        sumnum = num1 + num2
        res = self.transform(sumnum)
        return res

    def transform2num(self, l):
        _tmp = []
        while l:
            _tmp.append(l.val)
            l = l.next
        
        num = 0
        for i in range(len(_tmp)):
            bei = 10**i
            num += _tmp[i]*bei
        return num

    def transform(self, number):
        _tmp = []
        count = 0
        num = number
        while num:
            count += 1
            _tmp.append(num%10)
            num = num//10

        head = ListNode(0)
        p = head
        for index, i in enumerate(_tmp):
            p.val = i
            if index == len(_tmp)-1:
                p.next = None
            else:
                p.next = ListNode(None)
                p = p.next
          
        return head
