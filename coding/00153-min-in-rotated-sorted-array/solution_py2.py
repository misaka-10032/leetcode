# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        l = 0
        r = len(nums)-1
        while l < r and nums[l] > nums[r]:
            m = (l+r) // 2
            if nums[m] < nums[l]:
                # p in left half, m inclusive
                r = m
            else:
                # p in right half, m exclusive
                l = m + 1

        return nums[l]
