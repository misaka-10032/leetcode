# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        """ new_id -> old_id """
        ids = sorted(range(0, len(nums)), key=lambda k: nums[k])
        """ new_id -> num """
        nums = sorted(nums)
        """ Find indices """
        p, q = 0, len(nums)-1
        while p < q:
            if nums[p] + nums[q] == target:
                return sorted([ids[p]+1, ids[q]+1])
            while p < q and nums[p] + nums[q] < target:
                p += 1
            while p < q and nums[p] + nums[q] > target:
                q -= 1
