# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        curr_sum = 0
        best = -1
        for x in nums:
            curr_sum += x
            if curr_sum > best:
                best = curr_sum
            if curr_sum < 0:
                # reset and begin the next cohort
                curr_sum = 0
        if best < 0:
            return max(nums)
        else:
            return best
