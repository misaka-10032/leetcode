# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* dp[i][kc] = min_{kp!=kc}{ dp[i-1][kp]+costs[i][kc] }
* To reduce cost of O(k^2), we can do the precessing to narrow down the kp to choose from,
  i.e. we want the top 2 minimun costs till (i-1)th house
* Edge case: k == 1: not acceptable
"""


class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs or not costs[0]:
            return 0
        n = len(costs)
        k = len(costs[0])

        if n == 1:
            return min(costs[0])
        if k <= 1:
            return -1

        inf = 999999999
        dp = [[0] * k for _ in xrange(n)]
        dp[0] = costs[0]
        for i in xrange(1, n):
            # find the top 2 min costs
            c0 = inf
            k0 = None
            for kp in xrange(k):
                if dp[i - 1][kp] < c0:
                    c0 = dp[i - 1][kp]
                    k0 = kp
            c1 = inf
            k1 = None
            for kp in xrange(k):
                if dp[i - 1][kp] < c1 and kp != k0:
                    c1 = dp[i - 1][kp]
                    k1 = dp
            for kc in xrange(k):
                if kc != k0:
                    dp[i][kc] = c0 + costs[i][kc]
                else:
                    dp[i][kc] = c1 + costs[i][kc]
        return min(dp[-1])
