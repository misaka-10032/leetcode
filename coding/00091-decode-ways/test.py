# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.numDecodings('') == 0
    assert sol.numDecodings('0') == 0
    assert sol.numDecodings('9') == 1
    assert sol.numDecodings('01') == 0
    assert sol.numDecodings('10') == 1
    assert sol.numDecodings('26') == 2


def test_1():
    sol = Solution()
    assert sol.numDecodings('12034') == 1
