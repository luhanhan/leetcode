#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: removeOuterParentheses_1021.py
#Author: luhan 
#Created Time: 2019-06-10 15:29:56
############################

"""
    A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings, and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.

    A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B, with A and B nonempty valid parentheses strings.

    Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k, where P_i are primitive valid parentheses strings.

    Return S after removing the outermost parentheses of every primitive string in the primitive decomposition of S.

     

    Example 1:

    Input: "(()())(())"
    Output: "()()()"
    Explanation: 
    The input string is "(()())(())", with primitive decomposition "(()())" + "(())".
    After removing outer parentheses of each part, this is "()()" + "()" = "()()()".

    Example 2:

    Input: "(()())(())(()(()))"
    Output: "()()()()(())"
    Explanation: 
    The input string is "(()())(())(()(()))", with primitive decomposition "(()())" + "(())" + "(()(()))".
    After removing outer parentheses of each part, this is "()()" + "()" + "()(())" = "()()()()(())".

    Example 3:

    Input: "()()"
    Output: ""
    Explanation: 
    The input string is "()()", with primitive decomposition "()" + "()".
    After removing outer parentheses of each part, this is "" + "" = "".

     

    Note:

        S.length <= 10000
        S[i] is "(" or ")"
        S is a valid parentheses string

"""

class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        ll = []
        rr = []
        if len(S)>10000:
            return False
        res = ""
        for i in range(len(S)):
            if S[i] == '(':
                ll.append('(')
                res += '('
            else:
                ll.pop()
                res += ')'
                if len(ll)==0:
                    rr.append(res)
                    res = ""
       
        rrr = ''
        for r in rr:
            rrr += r[1:-1]
        return rrr 


s = Solution()
ss = "(()())(())(()(()))"
print ss
print s.removeOuterParentheses(ss)
