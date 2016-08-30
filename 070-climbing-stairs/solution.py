# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        f = [0] * (n+2)
        f[0] = 1
        for i in xrange(n):
            f[i+1] += f[i]
            f[i+2] += f[i]
        return f[n]
