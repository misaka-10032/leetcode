# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def _wiggle(self, nums, is_small):
        cnt = 1
        for i in xrange(1, len(nums)):
            if is_small and nums[i] < nums[i-1] or \
               not is_small and nums[i] > nums[i-1]:
                is_small = not is_small
                cnt += 1
        return cnt

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        return max(self._wiggle(nums, True), self._wiggle(nums, False))
