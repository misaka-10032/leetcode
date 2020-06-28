# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""


class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def matches(sc, pc):
            return sc == pc or pc == '.'

        s = '^' + s + '$'
        p = '^' + p + '$'
        m = len(s)
        n = len(p)
        f = [[False] * n for _ in xrange(m)]
        f[0][0] = True  # ^ == ^
        for j in xrange(1, n):
            for i in xrange(m):
                if p[j] != '*':
                    f[i][j] = i >= 1 and f[i-1][j-1] and matches(s[i], p[j])
                else:
                    f[i][j] = False
                    # Case 1: match one
                    # s:  ba
                    # p: ba*
                    f[i][j] |= f[i][j-1]

                    # Case 2: ignore
                    # s:   a
                    # p: ab*
                    f[i][j] |= j >= 2 and f[i][j-2]

                    # Case 3: continue
                    # s: aa
                    # p: a*
                    f[i][j] |= i >= 1 and f[i-1][j] and matches(s[i], p[j-1])
        return f[m-1][n-1]
