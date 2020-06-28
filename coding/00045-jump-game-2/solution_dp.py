# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        d = [-1] * len(nums)
        d[0] = 0
        for i in xrange(len(nums)-1):
            for j in xrange(1, nums[i]+1):
                if i+j >= len(nums):
                    break
                # relax
                w = d[i] + 1
                if d[i+j] < 0 or w < d[i+j]:
                    d[i+j] = w
        return d[-1]
