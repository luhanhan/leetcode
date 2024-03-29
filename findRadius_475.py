#!/usr/bin/python
#-*- coding:utf-8 -*-
############################
#File Name: findRadius_475.py
#Author: luhan 
#Created Time: 2019-06-18 15:19:11
############################
"""
Winter is coming! Your first job during the contest is to design a standard heater with fixed warm radius to warm all the houses.

Now, you are given positions of houses and heaters on a horizontal line, find out minimum radius of heaters so that all houses could be covered by those heaters.

So, your input will be the positions of houses and heaters seperately, and your expected output will be the minimum radius standard of heaters.

Note:

    Numbers of houses and heaters you are given are non-negative and will not exceed 25000.
    Positions of houses and heaters you are given are non-negative and will not exceed 10^9.
    As long as a house is in the heaters' warm radius range, it can be warmed.
    All the heaters follow your radius standard and the warm radius will the same.

 

Example 1:

Input: [1,2,3],[2]
Output: 1
Explanation: The only heater was placed in the position 2, and if we use the radius 1 standard, then all the houses can be warmed.

 

Example 2:

Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use radius 1 standard, then all the houses can be warmed.


解题思路：

排序（Sort） + 二分查找（Binary Search）

升序排列加热器的坐标heaters

遍历房屋houses，记当前房屋坐标为house：

    利用二分查找，分别找到不大于house的最大加热器坐标left，以及不小于house的最小加热器坐标right
    
    则当前房屋所需的最小加热器半径radius = min(house - left, right - house)
    
    利用radius更新最终答案ans

"""

class Solution(object):
    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        import bisect

        ans = 0
        heaters.sort()
        for house in houses:
            radius = 0x7FFFFFFF
            le = bisect.bisect_right(heaters, house)
            if le > 0:
                radius = min(radius, house - heaters[le - 1])
            ge = bisect.bisect_left(heaters, house)
            if ge < len(heaters):
                radius = min(radius, heaters[ge] - house)
            ans = max(ans, radius)
        return ans

s = Solution()
houses = [1,2,3] 
heaters = [2]
print s.findRadius(houses, heaters)
