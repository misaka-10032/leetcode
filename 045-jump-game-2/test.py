# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.jump([]) == 0
    assert sol.jump([10]) == 0


def test_1():
    sol = Solution()
    assert sol.jump([2, 3, 1, 1, 4]) == 2


def test_2():
    sol = Solution()
    assert sol.jump([1, 2, 3]) == 2


def test_3():
    sol = Solution()
    nums = ([0, 1] + range(1, 25001))[::-1]
    print sol.jump(nums)