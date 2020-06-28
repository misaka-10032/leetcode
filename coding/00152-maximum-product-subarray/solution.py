# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        best = _max = _min = nums[0]
        n = len(nums)
        for i in xrange(1, n):
            x = nums[i]
            a = x * _min
            b = x * _max
            _min = min(x, a, b)
            _max = max(x, a, b)
            best = max(best, _max)
        return best
