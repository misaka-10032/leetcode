# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        best = 0
        lowest = 999999999
        for c in prices:
            lowest = min(lowest, c)
            profit = c - lowest
            best = max(best, profit)
        return best
