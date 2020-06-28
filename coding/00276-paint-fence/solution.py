# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k

        prev_diff = k * (k-1)
        prev_same = k
        for _ in xrange(2, n):
            this_diff = (prev_diff+prev_same) * (k-1)
            this_same = prev_diff
            prev_diff, prev_same = this_diff, this_same
        return prev_diff + prev_same
