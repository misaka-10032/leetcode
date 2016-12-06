# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.validUtf8([])
    assert sol.validUtf8([0])
    assert sol.validUtf8([1, 1, 1, 1, 1])
    assert not sol.validUtf8([1, 1, 256])


def test_1():
    assert sol.validUtf8([197, 130, 1])
    assert not sol.validUtf8([235, 140, 4])


def test_2():
    assert sol.validUtf8([230, 136, 145])
