# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]:
            return []
        m = len(matrix)
        n = len(matrix[0])

        res = []
        i, j = 0, 0
        w = n - 1
        h = m - 1
        while w > 0 and h > 0:
            for dj in xrange(w):
                res.append(matrix[i][j+dj])
            j += w
            for di in xrange(h):
                res.append(matrix[i+di][j])
            i += h
            for dj in xrange(w):
                res.append(matrix[i][j-dj])
            j -= w
            for di in xrange(h):
                res.append(matrix[i-di][j])
            i -= h
            i += 1
            j += 1
            w -= 2
            h -= 2
        if w == 0:
            for di in xrange(h+1):
                res.append(matrix[i+di][j])
        elif h == 0:
            for dj in xrange(w+1):
                res.append(matrix[i][j+dj])
        return res
