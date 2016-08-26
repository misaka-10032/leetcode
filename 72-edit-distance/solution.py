# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1:
            return len(word2)
        if not word2:
            return len(word1)

        m = len(word1)
        n = len(word2)
        d = [[0] * n for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                d1 = 1 + (d[i-1][j] if i > 0 else j)
                d2 = 1 + (d[i][j-1] if j > 0 else i)
                d3 = d[i-1][j-1] if i > 0 and j > 0 else max(i, j)
                d3 += word1[i] != word2[j]
                d[i][j] = min(d1, d2, d3)
        return d[m-1][n-1]
