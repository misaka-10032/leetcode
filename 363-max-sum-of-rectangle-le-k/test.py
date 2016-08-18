# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution


def test_0():
    sol = Solution()
    assert sol.maxSumSubmatrix([], 10) == 0
    assert sol.maxSumSubmatrix([[]], 10) == 0


def test_1():
    sol = Solution()
    matrix = [[1, 0, 1], [0, -2, 3]]
    assert sol.maxSumSubmatrix(matrix, 2) == 2


def maxSumSubmatrix(matrix, k):
    m = len(matrix)
    n = len(matrix[0])
    sums = []
    for row in matrix:
        sums.append(list(row))
    for i in xrange(1, m):
        for j in xrange(n):
            sums[i][j] += sums[i-1][j]
    for i in xrange(m):
        for j in xrange(1, n):
            sums[i][j] += sums[i][j-1]

    best = -999999999
    for p in xrange(m):
        for q in xrange(n):
            for i in xrange(p, m):
                for j in xrange(q, n):
                    anchor_pq = 0 if p == 0 or q == 0 else sums[p-1][q-1]
                    anchor_p = 0 if p == 0 else sums[p-1][j]
                    anchor_q = 0 if q == 0 else sums[i][q-1]
                    candidate = sums[i][j] - anchor_p - anchor_q + anchor_pq
                    if best < candidate <= k:
                        best = candidate
    return best


def test_2():
    sol = Solution()
    m = n = 50
    for _ in xrange(5):
        matrix = np.random.randint(-100, 100, (m, n)).tolist()
        k = np.random.randint(-400, 400)
        assert sol.maxSumSubmatrix(matrix, k) == maxSumSubmatrix(matrix, k)


def test_3():
    sol = Solution()
    matrix = [[2, 2, -1]]
    assert maxSumSubmatrix(matrix, 0) == -1
    assert sol.maxSumSubmatrix(matrix, 0) == -1


def test_4():
    sol = Solution()
    matrix = [[5, -4, -3, 4], [-3, -4, 4, 5], [5, 1, 5, -4]]
    assert maxSumSubmatrix(matrix, 3) == 2
    assert sol.maxSumSubmatrix(matrix, 3) == 2
