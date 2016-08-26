# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.maximalSquare([]) == 0
    assert sol.maximalSquare([[]]) == 0
    assert sol.maximalSquare([['1']]) == 1


def test_1():
    sol = Solution()
    matrix = [['1', '0', '1', '0', '0'],
              ['1', '0', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]
    assert sol.maximalSquare(matrix) == 4


def test_2():
    sol = Solution()
    matrix = [['1', '1', '1', '0', '0'],
              ['1', '1', '1', '1', '1'],
              ['1', '1', '1', '1', '1'],
              ['1', '0', '0', '1', '0']]
    assert sol.maximalSquare(matrix) == 9
