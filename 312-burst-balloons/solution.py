# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

TODO: purpose
"""


class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0

        scores = [[0 for _ in xrange(l)] for _ in xrange(l)]
        for i in xrange(l):
            left = nums[i-1] if i-1 >= 0 else 1
            right = nums[i+1] if i+1 < l else 1
            scores[i][i] = left * nums[i] * right

        for delta in xrange(1, l):
            for start in xrange(l-delta):
                end = start + delta
                best = -1
                for k in xrange(start, end+1):
                    left = scores[start][k-1] if k-1 >= 0 else 0
                    right = scores[k+1][end] if k+1 < l else 0
                    s = left + right

                    left = nums[start-1] if start-1 >= 0 else 1
                    right = nums[end+1] if end+1 < l else 1
                    s += left * nums[k] * right

                    if s > best:
                        best = s

                scores[start][end] = best

        return scores[0][l-1]
