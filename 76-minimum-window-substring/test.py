# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.minWindow('abc', '') == ''
    assert sol.minWindow('abc', 'a') == 'a'
    assert sol.minWindow('abc', 'abc') == 'abc'
    assert sol.minWindow('abc', 'abcd') == ''


def test_1():
    sol = Solution()
    assert sol.minWindow('ADOBECODEBANC', 'ABC') == 'BANC'
