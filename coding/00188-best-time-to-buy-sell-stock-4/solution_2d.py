# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n <= 1:
            return 0

        f = [[0] * (n+1) for _ in xrange(k+1)]
        for i in xrange(1, k+1):
            opt = -prices[0]
            for j in xrange(1, n+1):
                p1 = f[i][j-1]
                p2 = prices[j-1] + opt
                f[i][j] = max(p1, p2)
                """ in next j's eye l is up to j-2 """
                opt = max(opt, f[i-1][j-1]-prices[j-1])
        return f[k][n]
