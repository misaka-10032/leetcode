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
        # previous 2 and previous 1
        p2 = p1 = 0
        for x in nums:
            # choice 1, do not rob this
            c1 = p1
            # choice 2, rob this
            c2 = p2 + x
            # final choice
            c = max(c1, c2)
            p2, p1 = p1, c
        return p1
