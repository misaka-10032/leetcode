# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m = len(matrix)
        n = len(matrix[0])
        l, r = 0, m*n-1
        while l < r:
            k = (l+r) // 2
            i, j = k//n, k%n
            if matrix[i][j] < target:
                l = k + 1
            elif matrix[i][j] > target:
                r = k - 1
            else:
                return True
        i, j = l//n, l%n
        if matrix[i][j] == target:
            return True
        else:
            return False
