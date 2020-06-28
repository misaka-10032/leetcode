# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        need to remove inplace...

        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return 1

        n = 1
        prev = nums[0]
        for i in xrange(1, len(nums)):
            x = nums[i]
            if x != prev:
                nums[n] = x
                n += 1
                prev = x

        return n
