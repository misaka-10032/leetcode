# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.findMin([]) == 0
    assert sol.findMin([2]) == 2
    assert sol.findMin([1, 2]) == 1
    assert sol.findMin([2, 1]) == 1
    assert sol.findMin([1, 1]) == 1
    assert sol.findMin([1, 1, 1]) == 1
    assert sol.findMin([1, 1, 1, 1]) == 1
    assert sol.findMin([1, 1, 1, 1, 1]) == 1


def test_1():
    sol = Solution()
    assert sol.findMin([0, 1, 2, 3, 4, 5, 6, 7]) == 0
    assert sol.findMin([7, 0, 1, 2, 3, 4, 5, 6]) == 0
    assert sol.findMin([6, 7, 0, 1, 2, 3, 4, 5]) == 0
    assert sol.findMin([5, 6, 7, 0, 1, 2, 3, 4]) == 0
    assert sol.findMin([4, 5, 6, 7, 0, 1, 2]) == 0


def test_2():
    sol = Solution()
    assert sol.findMin([5, 6, 7, 8, 9, 1, 2, 3, 4]) == 1


def test_3():
    sol = Solution()
    assert sol.findMin([5, 6, 7, 8, 1, 2, 5]) == 1
    assert sol.findMin([5, 5, 6, 7, 7, 8, 1, 1, 2, 5]) == 1
    assert sol.findMin([5, 5, 6, 7, 7, 8, 1, 1, 2, 5, 5]) == 1


def test_4():
    sol = Solution()
    assert sol.findMin([3, 1]) == 1


def test_5():
    sol = Solution()
    assert sol.findMin([3, 3, 1]) == 1


def test_6():
    sol = Solution()
    assert sol.findMin([10, 1, 10, 10, 10]) == 1
