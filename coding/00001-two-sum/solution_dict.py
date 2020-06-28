# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        v_to_i = {}
        for i, v in enumerate(nums):
            v_to_i[v] = i
        for i, v in enumerate(nums):
            c = target - v
            if c in v_to_i:
                j = v_to_i[c]
                if i != j:
                    return sorted([i, j])
