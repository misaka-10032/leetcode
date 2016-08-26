# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) <= 1:
            return True
        l_curr = 0            # lower bound of the cohort
        r_curr = nums[0]      # upper bound of the cohort
        last = len(nums) - 1
        while r_curr < last:
            r_next = r_curr
            for i in xrange(l_curr, r_curr + 1):
                r_next = max(r_next, i + nums[i])
            if r_next == r_curr:
                return False  # unreachable
            l_curr, r_curr = r_curr + 1, r_next
        return True
