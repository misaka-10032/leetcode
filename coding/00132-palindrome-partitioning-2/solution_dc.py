# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        def _min_cut(i, j):
            if (i, j) in cache:
                return cache[(i, j)]
            best = j-i
            for k in xrange(i+1, j):
                r = 1 + _min_cut(i, k) + _min_cut(k, j)
                best = min(best, r)
            cache[(i, j)] = best
            return best

        n = len(s)
        # prepare palindromes
        cache = {}
        for i in xrange(n):
            cache[(i, i)] = 0
            cache[(i, i+1)] = 0
        for sz in xrange(2, n+1):
            for i in xrange(n+1-sz):
                j = i + sz
                if s[i] == s[j-1] and (i+1, j-1) in cache:
                    cache[(i, j)] = 0
        # divide and conquer
        return _min_cut(0, n)
