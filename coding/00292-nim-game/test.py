# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.canWinNim(1)
    assert sol.canWinNim(2)
    assert sol.canWinNim(3)
    assert not sol.canWinNim(4)


def test_1():
    assert not sol.canWinNim(128)
    assert not sol.canWinNim(132)
    assert sol.canWinNim(134)
    assert not sol.canWinNim(1348820612)
