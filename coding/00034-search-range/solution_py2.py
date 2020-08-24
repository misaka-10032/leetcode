# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def _find(self, nums, target):
        li, ri = 0, len(nums)-1
        while li < ri:
            mi = (li + ri) // 2
            if nums[mi] > target:
                ri = mi - 1
            elif nums[mi] < target:
                li = mi + 1
            else:
                return mi
        if li == ri and nums[li] == target:
            return li
        else:
            return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return [-1, -1]

        if len(nums) == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        k = l = r = self._find(nums, target)

        if k == -1:
            return [-1, -1]

        while l >= 0 and nums[l] == nums[k]:
            l -= 1
        while r < len(nums) and nums[r] == nums[k]:
            r += 1
        return [l+1, r-1]
