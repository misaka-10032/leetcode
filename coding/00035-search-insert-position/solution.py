# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0

        if len(nums) == 1:
            if nums[0] >= target:
                return 0
            else:
                return 1

        li, ri = 0, len(nums)-1
        while li < ri:
            mi = (li + ri) // 2
            if nums[mi] < target:
                li = mi + 1
            elif nums[mi] > target:
                ri = mi - 1
            else:
                return mi

        if li == ri:
            if nums[li] >= target:
                return li
            else:
                return li + 1

        """ now ri+1 == li """

        if ri == -1:
            if target < nums[li]:
                return li
            else:  # won't be equal
                return li + 1

        if li == len(nums):
            if target < nums[ri]:
                return ri
            else:
                return li

        if target < nums[ri] < nums[li]:
            return ri
        elif nums[ri] < target < nums[li]:
            return li
        else:
            return li + 1
