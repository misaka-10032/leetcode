# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        def subsum(i, j):
            """ sub sum in [i, j) """
            return nums[j-1] - (nums[i-1] if i > 0 else 0)
        n = len(nums)
        for i in xrange(1, n):
            nums[i] += nums[i-1]
        i = 0
        best = n+1
        for j in xrange(1, n+1):
            if subsum(i, j) < s:
                continue
            while i < j:
                if subsum(i+1, j) >= s:
                    i += 1
                else:
                    break
            best = min(best, j-i)
        return best if best <= n else 0
