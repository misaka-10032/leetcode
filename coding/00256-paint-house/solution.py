# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* dp[i][k] = min_{kk!=k}{ dp[i-1][kk]+costs[i][k] }
"""


class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        n = len(costs)
        if n == 0:
            return 0
        elif n == 1:
            return min(costs[0])

        inf = 999999999
        dp = [[0] * 3 for _ in xrange(n)]
        dp[0] = costs[0]
        for i in xrange(1, n):
            for k in xrange(3):
                best = inf  # min prev cost
                for kk in xrange(3):
                    if k == kk:
                        continue
                    best = min(best, dp[i - 1][kk])
                dp[i][k] = best + costs[i][k]
        return min(dp[-1])
