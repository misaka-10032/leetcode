# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class NumMatrix(object):
    def __init__(self, matrix):
        """
        initialize your data structure here.
        :type matrix: List[List[int]]
        """
        if not matrix:
            matrix = [[]]
        self.m = len(matrix)
        self.n = len(matrix[0])
        self.matrix = [[0] * self.n for _ in xrange(self.m)]
        self.bit = [[0] * (self.n+1) for _ in xrange(self.m+1)]
        for i in xrange(self.m):
            for j in xrange(self.n):
                self.update(i, j, matrix[i][j])

    def update(self, row, col, val):
        """
        update the element at matrix[row,col] to val.
        :type row: int
        :type col: int
        :type val: int
        :rtype: void
        """
        dv = val - self.matrix[row][col]
        self.matrix[row][col] = val
        i = row + 1
        while i <= self.m:
            j = col + 1
            while j <= self.n:
                self.bit[i][j] += dv
                j += j & -j
            i += i & -i

    def prefix(self, row, col):
        s = 0
        i = row + 1
        while i > 0:
            j = col + 1
            while j > 0:
                s += self.bit[i][j]
                j -= j & -j
            i -= i & -i
        return s

    def sumRegion(self, row1, col1, row2, col2):
        """
        sum of elements matrix[(row1,col1)..(row2,col2)], inclusive.
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.prefix(row2, col2) + self.prefix(row1-1, col1-1) \
               - self.prefix(row1-1, col2) - self.prefix(row2, col1-1)
