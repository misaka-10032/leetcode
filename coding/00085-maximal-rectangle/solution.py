# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        if not matrix[0]:
            return 0
        m = len(matrix)
        n = len(matrix[0])

        best = 0
        height = [0] * n
        left = [0] * n
        right = [n] * n
        for i in xrange(m):
            for j in xrange(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0
            leftmost = 0
            for j in xrange(n):
                if matrix[i][j] == '1':
                    # compare leftmost from previous row and current row
                    left[j] = max(left[j], leftmost)
                else:
                    left[j] = 0       # don't affect the next row when doing max
                    leftmost = j + 1  # prepare for the next 1
            rightmost = n
            for j in reversed(xrange(n)):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], rightmost)
                else:
                    right[j] = n      # don't affect the next row when doing min
                    rightmost = j     # prepare for the prev 1
            for j in xrange(n):
                if matrix[i][j] == '1':
                    best = max(best, (right[j]-left[j])*height[j])
        return best
