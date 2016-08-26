# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


from solution import Solution


def test_0():
    sol = Solution()
    assert sol.minDistance('', 'abc') == 3
    assert sol.minDistance('ddde', '') == 4


def test_1():
    sol = Solution()
    assert sol.minDistance('abcd', 'abce') == 1
    assert sol.minDistance('abc', 'abcd') == 1
    assert sol.minDistance('abcd', 'abc') == 1


def test_2():
    sol = Solution()
    assert sol.minDistance('acdf', 'bcd') == 2


def test_3():
    sol = Solution()
    assert sol.minDistance('ab', 'bc') == 2
