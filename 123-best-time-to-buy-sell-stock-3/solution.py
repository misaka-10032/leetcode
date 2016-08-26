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
        n = len(prices)
        if n <= 1:
            return 0
        fwd = [0] * n
        bwd = [0] * n
        inf = 999999999

        lowest = inf
        for i, c in enumerate(prices):
            lowest = min(lowest, c)
            prev = fwd[i-1] if i > 0 else -inf
            fwd[i] = max(prev, c-lowest)

        highest = -inf
        for i in xrange(n-1, -1, -1):
            c = prices[i]
            highest = max(highest, c)
            prev = bwd[i+1] if i < n-1 else -inf
            bwd[i] = max(prev, highest-c)

        profits = [fwd[i]+bwd[i] for i in xrange(n)]
        return max(profits)
