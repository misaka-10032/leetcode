# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def get(i):
            return nums[i] if 0 <= i < n else -inf

        if not nums:
            return -1

        inf = 999999999
        n = len(nums)
        l, r = 0, n-1
        while l + 2 < r:
            m = (l+r) // 2
            if get(m) > get(m+1):
                r = m
            else:
                l = m
        return max(range(l, r+1), key=lambda i: nums[i])
