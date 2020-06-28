# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        dist = [-1] * len(nums)
        Q = deque()
        dist[0] = 0
        Q.append(0)

        while dist[-1] < 0:
            i = Q.popleft()
            for s in xrange(nums[i], 0, -1):
                if i+s < len(nums) and dist[i+s] < 0:
                    dist[i+s] = 1 + dist[i]
                    Q.append(i+s)

        return dist[-1]
