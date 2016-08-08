# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def _find_pivot(self, nums):
        li, ri = 0, len(nums)-1
        while li < ri:
            mi = (li+ri)//2
            if nums[mi] > nums[ri]:
                # pivot will be on the right, exclusive
                li = mi + 1
            elif nums[mi] < nums[ri]:
                # pivot will be on the left, inclusive
                ri = mi
            else:
                # as there's no duplicate
                assert mi == ri
        assert li == ri
        return li

    def _find_within(self, nums, target, li, ri):
        while li < ri:
            mi = (li+ri)//2
            if target > nums[mi]:
                li = mi + 1
            elif target < nums[mi]:
                ri = mi - 1
            else:
                return mi
        if li == ri and nums[li] == target:
            return li
        else:
            return -1

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1

        if len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1

        p = self._find_pivot(nums)

        if p == 0:
            return self._find_within(nums, target, 0, len(nums) - 1)

        if nums[p] <= target <= nums[-1]:
            return self._find_within(nums, target, p, len(nums) - 1)
        elif nums[0] <= target <= nums[p-1]:
            return self._find_within(nums, target, 0, p - 1)
        else:
            return -1
