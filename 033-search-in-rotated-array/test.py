# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.search([], 10) == -1
    assert sol.search([1], 1) == 0
    assert sol.search([100], 1) == -1


def test_1():
    sol = Solution()
    sol.search([0, 1, 2, 3, 4, 5], 0) == 0
    sol.search([0, 1, 2, 3, 4, 5], 5) == 5
    sol.search([0, 1, 2, 3, 4, 5], 2) == 2
    sol.search([0, 1, 2, 3, 4, 5], 2.5) == -1
    sol.search([0, 1, 2, 3, 4], 0) == 0
    sol.search([0, 1, 2, 3, 4], 4) == 4
    sol.search([0, 1, 2, 3, 4], 1) == 1


def test_2():
    sol = Solution()
    sol.search([4, 5, 6, 7, 0, 1, 2], 4) == 0
    sol.search([4, 5, 6, 7, 0, 1, 2], 2) == 6
    sol.search([4, 5, 6, 7, 0, 1, 2], 3) == -1
    sol.search([4, 5, 6, 7, 0, 1, 2], 5) == 1

