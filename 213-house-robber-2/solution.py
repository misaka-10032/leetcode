# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def _rob(start, end):
            # previous 2 and previous 1
            p2 = p1 = 0
            for i in xrange(start, end):
                x = nums[i]
                # choice 1, do not rob this
                c1 = p1
                # choice 2, rob this
                c2 = p2 + x
                # final choice
                c = max(c1, c2)
                p2, p1 = p1, c
            return p1

        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max(_rob(0, n-1), _rob(1, n))
