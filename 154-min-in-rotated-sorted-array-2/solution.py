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
        while l < r and nums[l] >= nums[r]:
            m = (l+r) // 2
            if nums[m] > nums[l]:
                l = m + 1
            elif nums[m] < nums[l]:
                r = m
            else:
                """ Tricky disturbance """
                l += 1
        return nums[l]
