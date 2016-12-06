# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.kSmallestPairs([], [], 0) == []
    assert sol.kSmallestPairs([1], [2], 1) == [[1, 2]]
    assert sol.kSmallestPairs([1, 2], [3, 5], 1) == [[1, 3]]
    assert sol.kSmallestPairs([1, 2], [3, 5], 2) == [[1, 3], [2, 3]]
    assert sol.kSmallestPairs([1, 2], [3, 5], 3) == [[1, 3], [2, 3], [1, 5]]
    assert sol.kSmallestPairs([1, 5], [2, 3], 1) == [[1, 2]]
    assert sol.kSmallestPairs([1, 5], [2, 3], 2) == [[1, 2], [1, 3]]
    assert sol.kSmallestPairs([1, 5], [2, 3], 3) == [[1, 2], [1, 3], [5, 2]]


def test_1():
    assert sol.kSmallestPairs([1, 7, 11], [2, 4, 6], 3) == [[1, 2], [1, 4], [1, 6]]
    assert sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 2) == [[1, 1], [1, 1]]


def test_2():
    assert sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 10) == \
           sol.kSmallestPairs([1, 1, 2], [1, 2, 3], 9)


def test_3():
    assert sol.kSmallestPairs([1, 2, 3, 4, 5, 6], [3, 5, 7, 9], 20) == \
           [[1, 3], [2, 3], [1, 5], [3, 3], [2, 5], [4, 3], [1, 7], [3, 5], [5, 3], [2, 7], [4, 5], [6, 3], [1, 9],
            [3, 7], [5, 5], [2, 9], [4, 7], [6, 5], [3, 9], [5, 7]]