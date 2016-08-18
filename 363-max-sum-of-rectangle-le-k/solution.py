# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import bisect


class Solution(object):
    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        S = []
        for row in matrix:
            S.append(list(row))
        for i in xrange(1, m):
            for j in xrange(n):
                S[i][j] += S[i-1][j]
        for i in xrange(m):
            for j in xrange(1, n):
                S[i][j] += S[i][j-1]

        best = -999999999
        for j in xrange(n):
            for q in xrange(j, n):
                T = [0] * m
                for p in xrange(m):
                    anchor = S[p][j-1] if j != 0 else 0
                    T[p] = S[p][q] - anchor
                neg_acc = []
                for i in xrange(m-1, -1, -1):
                    bisect.insort(neg_acc, -T[i])
                    anchor = T[i-1] if i != 0 else 0
                    idx = bisect.bisect_left(neg_acc, -k-anchor)
                    if idx != len(neg_acc):
                        candidate = -neg_acc[idx] - anchor
                        best = max(best, candidate)
        return best
