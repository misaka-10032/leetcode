# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        sz = 0
        for i in xrange(n):
            if nums[i] != 0:
                nums[sz] = nums[i]
                sz += 1
        for i in xrange(sz, n):
            nums[i] = 0
