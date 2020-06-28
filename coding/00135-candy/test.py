# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.candy([]) == 0
    assert sol.candy([10]) == 1


def test_1():
    sol = Solution()
    assert sol.candy([3, 4, 5, 6]) == 10
    assert sol.candy([6, 5, 4, 3]) == 10
    assert sol.candy([2, 2, 2, 2]) == 4


def test_2():
    sol = Solution()
    assert sol.candy([5, 2, 5, 2, 1]) == 9
    ratings = [3, 4, 7, 6, 5, 4, 4, 4, 5, 6, 6, 6, 5, 4]
    candies = [1, 2, 4, 3, 2, 1, 1, 1, 2, 3, 1, 3, 2, 1]
    assert sol.candy(ratings) == sum(candies)
