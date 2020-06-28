# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert not sol.search([], 1)
    assert sol.search([2], 2)
    assert not sol.search([2], 1)
    assert sol.search([1, 2], 1)
    assert sol.search([2, 1], 1)
    assert sol.search([1, 1], 1)
    assert not sol.search([1, 1, 1], 2)


def test_1():
    assert sol.search([5, 6, 7, 8, 1, 2, 5], 5)
    assert sol.search([5, 6, 7, 8, 1, 2, 5], 1)
    assert sol.search([5, 6, 7, 8, 1, 2, 5], 7)
    assert not sol.search([5, 6, 7, 8, 1, 2, 5], 9)
    assert not sol.search([5, 6, 7, 8, 1, 2, 5], 0)
    assert not sol.search([5, 6, 7, 8, 1, 2, 5], 3)
    assert sol.search([5, 5, 6, 7, 7, 8, 1, 1, 2, 5, 5], 5)
    assert sol.search([5, 5, 6, 7, 7, 8, 1, 1, 2, 5, 5], 7)
    assert sol.search([5, 5, 6, 7, 7, 8, 1, 1, 2, 5, 5], 2)


def test_2():
    assert sol.search([10, 1, 10, 10, 10], 1)
    assert sol.search([10, 1, 10, 10, 10], 10)
    assert not sol.search([10, 1, 10, 10, 10], 9)
    assert not sol.search([10, 1, 10, 10, 10], 2)


def test_3():
    assert sol.search([1, 3, 5], 3)
