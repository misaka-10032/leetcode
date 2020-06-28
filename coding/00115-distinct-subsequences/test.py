# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.numDistinct('', '') == 0
    assert sol.numDistinct('a', 'ab') == 0
    assert sol.numDistinct('ab', '') == 0
    assert sol.numDistinct('ab', 'ab') == 1


def test_1():
    sol = Solution()
    assert sol.numDistinct('rabbbit', 'rabbit') == 3
    assert sol.numDistinct('rabbbbit', 'rabbit') == 6


def test_2():
    sol = Solution()
    assert sol.numDistinct('ccc', 'c') == 3
