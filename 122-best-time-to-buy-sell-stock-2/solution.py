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
        profit = 0
        bought = None
        for i in xrange(len(prices)-1):
            if bought is None and prices[i+1] > prices[i]:
                bought = prices[i]
            elif bought is not None and prices[i+1] < prices[i]:
                profit += prices[i] - bought
                bought = None
        if bought is not None:
            # end last transaction
            profit += prices[-1] - bought
        return profit
