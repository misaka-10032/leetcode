# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert not sol.canWin('')
    assert not sol.canWin('+')
    assert sol.canWin('++')
    assert sol.canWin('+++')
    assert sol.canWin('++++')


def test_1():
    assert sol.canWin('+++--++++')
    assert not sol.canWin('+++++')
    assert sol.canWin('++++++')
    assert sol.canWin('+++++++')
    assert sol.canWin('++++++++')
    assert not sol.canWin('+++++++++')
    assert not sol.canWin('+++++---+++++')
    assert sol.canWin('++++++++---+++++')
    sol.canWin('+'*12)
