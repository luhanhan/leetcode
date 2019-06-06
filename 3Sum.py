#coding=utf-8
"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        if not nums:
            return []
        
        length = len(nums)
        if length < 3:
            return []
        elif length == 3:
            if sum(nums) == 0:
                return [nums]

       # res = []
       # nums.sort()
       # for i in xrange(len(nums)-2):
       #     if i > 0 and nums[i] == nums[i-1]:
       #         continue
       #     l, r = i+1, len(nums)-1
       #     while l < r:
       #         s = nums[i] + nums[l] + nums[r]
       #         if s < 0:
       #             l +=1 
       #         elif s > 0:
       #             r -= 1
       #         else:
       #             res.append((nums[i], nums[l], nums[r]))
       #             while l < r and nums[l] == nums[l+1]:
       #                 l += 1
       #             while l < r and nums[r] == nums[r-1]:
       #                 r -= 1
       #             l += 1; r -= 1
       # return res

        nums = sorted(nums)
        for index in xrange(length-2):
            if index > 0 and nums[index]==nums[index-1]:
                continue
            jindex = index+1
            kindex = length-1
            while jindex < kindex:
                _sum = nums[index] + nums[jindex] + nums[kindex]
                if _sum > 0:
                    kindex -= 1
                elif _sum < 0:
                    jindex += 1
                else:
                    res.append([nums[index], nums[jindex], nums[kindex]])
                    while jindex < kindex and nums[jindex] == nums[jindex+1]:
                        jindex += 1
                    while jindex < kindex and nums[kindex] == nums[kindex-1]:
                        kindex -= 1
                    jindex += 1
                    kindex -= 1
               
        return res

s = Solution()
nums = [-1,0,1,2,-1,-4]
nums = [1,2,-2,-1]
nums = [-1,0,1,2,-1,-4]
nums = [3,0,-2,-1,1,2]
nums = [-1, 0, 1, 2, -1, 4]
nums = [0, 0, 0]
nums = [0,0,0,0]
nums = [-2,0,1,1,2]
print s.threeSum(nums)
