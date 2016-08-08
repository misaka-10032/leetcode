# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        sz = 0
        for i in xrange(len(nums)):
            x = nums[i]
            if x != val:
                nums[sz] = x
                sz += 1
        return sz
