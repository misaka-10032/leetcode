# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import bisect


class Solution(object):
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0

        inf = 999999999
        n = len(envelopes)
        vals = sorted(envelopes, key=lambda x: (x[0], -x[1]))
        vals = map(lambda x: x[1], vals)
        tails = [inf] * (n+1)
        tails[0] = vals[0]

        for i in xrange(1, n):
            """
            find p such that
            tails[j] <  tails[p], for j in [0, p)
            tails[k] >= tails[p], for k in [p, i)
            """
            v = vals[i]
            p = bisect.bisect_left(tails, v, 0, i)
            tails[p] = min(tails[p], v)

        i = n - 1
        while i > 0:
            if tails[i] != inf:
                break
            i -= 1
        return i + 1
