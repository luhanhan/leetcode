#coding=utf-8
#coding=utf-8
"""
    Given the root node of a binary search tree, return the sum of vals of all nodes with val between L and R (inclusive).

    The binary search tree is guaranteed to have unique vals.

     
    Example 1:

    Input: root = [10,5,15,3,7,null,18], L = 7, R = 15
    Output: 32

    Example 2:

    Input: root = [10,5,15,3,7,13,18,1,null,6], L = 6, R = 10
    Output: 23


    Note:

        The number of nodes in the tree is at most 10000.
        The final answer is guaranteed to be less than 2^31.

    深度优先算法

"""


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        self.summ = 0 
        self.dfs(root, L, R)
        return self.summ

    def dfs(self, root, L, R):
        if not root:
            return
        if root.val >= L and root.val <= R:
            self.summ += root.val
            self.dfs(root.left, L, R)
            self.dfs(root.right, L, R)                                                              
        elif root.val < L:
            self.dfs(root.right, L, R)
        elif root.val > R: 
            self.dfs(root.left, L, R)


s = Solution()
root = [10,5,15,3,7,null,18]
L = 7
R = 15
print s.rangeSumBST(root, L, R)
