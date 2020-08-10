# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        n = len(nums)
        if n < k or k <= 0:
            return []

        q = deque()
        for i in xrange(k):
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)

        res = [nums[q[0]]]
        for i in xrange(k, n):
            # pop those out of window first
            while q and q[0] <= i - k:
                q.popleft()
            # ensure decreasing
            while q and nums[q[-1]] <= nums[i]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res
