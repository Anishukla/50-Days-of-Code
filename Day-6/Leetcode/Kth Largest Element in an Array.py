# -*- coding: utf-8 -*-
"""
@author: anishukla
"""
# Level: Easy

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = sorted(nums,reverse=True)
        res = nums[k-1]
        return res