# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s or not t:
            return 0
        m = len(s)
        n = len(t)
        if m < n:
            return 0

        f = [[0] * (n+1) for _ in xrange(m+1)]
        for i in xrange(m+1):
            f[i][0] = 1
        for i in xrange(1, m+1):
            for j in xrange(1, min(m+1, n+1)):
                f[i][j] = f[i-1][j]
                if s[i-1] == t[j-1]:
                    f[i][j] += f[i-1][j-1]
        return f[m][n]
