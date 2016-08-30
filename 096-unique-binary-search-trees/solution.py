# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        g = [0] * (n+1)
        g[0] = 1
        # compute g[k]
        for k in xrange(1, n+1):
            # with i = 0 .. k-1
            for i in xrange(k):
                g[k] += g[i] * g[k-i-1]
        return g[n]
