#coding=utf-8
"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"

"""



class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
       # length = 0
       # temp_list = []
       # last = -1
       # for i in range(len(s)):
       #     if s[i] not in ['(', ')']:
       #         return 0
       #     if s[i]=='(':
       #         temp_list.append(s[i])
       #     elif s[i]==')':
       #         if not temp_list:
       #             last = i
       #         temp_list.pop()
       #         if not temp_list:
       #             temp_list.append(i)
       #         else:
       #             length = max(length, i-temp_list[-1])
       # return length

        maxlen = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i) # push the INDEX into the stack!!!!
            else:
                stack.pop() 
                if stack == []: 
                    stack.append(i)
                else: 
                    maxlen = max(maxlen, i-stack[-1])
        
        return maxlen


s = Solution()
ss = ')()())'
print s.longestValidParentheses(ss)
#ss = '(()'
#print s.longestValidParentheses(ss)
#ss = '('
#print s.longestValidParentheses(ss)
#ss = ")()())"
#print s.longestValidParentheses(ss)
ss = "()(())"
print s.longestValidParentheses(ss)
