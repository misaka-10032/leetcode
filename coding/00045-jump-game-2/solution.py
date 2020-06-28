# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return 0
        k = 1                 # kth cohort
        l_curr = 0            # lower bound of the cohort
        r_curr = nums[0]      # upper bound of the cohort
        last = len(nums) - 1
        while r_curr < last:
            r_next = r_curr
            for i in xrange(l_curr, r_curr+1):
                r_next = max(r_next, i+nums[i])
            if r_next == r_curr:
                return -1      # unreachable
            k += 1
            l_curr, r_curr = r_curr+1, r_next
        return k
