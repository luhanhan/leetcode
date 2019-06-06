#coding=utf-8
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return None
        
        res = None
        original = nums
        _nums = sorted(nums)
        for i,n in enumerate(_nums):
            m = target-n
            if m in _nums[i:]:
                if m == n:
                    indexs = [i for i in range(len(nums)) if nums[i]==n]
                    return indexs[0:2]
                else:
                    return [nums.index(n), nums.index(m)]
            else:
                continue


s = Solution()
nums = [-1,-2,-3,-4,-5]
target = -8
print s.twoSum(nums, target)
