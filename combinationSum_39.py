#coding=utf-8
"""
    Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

    The same repeated number may be chosen from candidates unlimited number of times.

    Note:

        All numbers (including target) will be positive integers.
        The solution set must not contain duplicate combinations.

    Example 1:

    Input: candidates = [2,3,6,7], target = 7,
    A solution set is:
    [
      [7],
      [2,2,3]
    ]

    Example 2:

    Input: candidates = [2,3,5], target = 8,
    A solution set is:
    [
      [2,2,2,2],
      [2,3,3],
      [3,5]
    ]

"""

class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        candidates = sorted(candidates)
        self.solver(candidates, target, res, path, 0)
        print res


    def solver(self, candidates, target, res, path, index):

        for i in range(index, len(candidates)):
            new_target = target-candidates[i]
            if new_target < 0:
                return
            else:
                if new_target == 0:
                    res.append(path + [candidates[i]])
                else:
                    self.solver(candidates, new_target, res, path+[candidates[i]], i)
            
            

s = Solution()
candidates = [2,3,5]
target = 8 
s.combinationSum(candidates, target)
