# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import bisect


class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        inf = 999999999
        n = len(nums)
        tails = [inf] * (n+1)
        tails[0] = nums[0]

        for i in xrange(1, n):
            """
            find p in [0:i), such that
            a[j] <  a[p] for j in [0, p)
            a[k] >= a[p] for k in [p, i)
            """
            v = nums[i]
            p = bisect.bisect_left(tails, v, 0, i)
            # append to tails[p-1], try update tails[p]
            tails[p] = min(tails[p], v)

        i = n - 1
        while i > 0:
            if tails[i] != inf:
                break
            i -= 1
        return i+1
