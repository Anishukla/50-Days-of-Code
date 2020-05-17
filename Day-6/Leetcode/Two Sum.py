# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
# Level: Easy

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        di = {}
        for i in range(len(nums)):
            val = target-nums[i]
            if val in di:
                L = [di[val], i]
                break
            di.update({nums[i]:i})
        return L