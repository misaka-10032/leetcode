# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        res = [1] * n
        left = 1
        for i in xrange(1, n):
            left *= nums[i-1]
            res[i] = left
        right = 1
        for i in xrange(n-2, -1, -1):
            right *= nums[i+1]
            res[i] *= right
        return res
