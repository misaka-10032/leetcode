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

        # reduced to greedy
        if k >= n//2:
            profit = 0
            bought = None
            for i in xrange(len(prices) - 1):
                if bought is None and prices[i + 1] > prices[i]:
                    bought = prices[i]
                elif bought is not None and prices[i + 1] < prices[i]:
                    profit += prices[i] - bought
                    bought = None
            if bought is not None:
                # end last transaction
                profit += prices[-1] - bought
            return profit

        prev = [0] * (n+1)
        for i in xrange(1, k+1):
            curr = [0] * (n+1)
            opt = -prices[0]
            for j in xrange(1, n+1):
                p1 = curr[j-1]
                p2 = prices[j-1] + opt
                curr[j] = max(p1, p2)
                """ in next j's eye l is up to j-2 """
                opt = max(opt, prev[j-1]-prices[j-1])
            prev = curr
        return prev[n]
