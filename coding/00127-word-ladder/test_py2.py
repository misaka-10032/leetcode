# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    wl = ['dot, cat']
    assert sol.ladderLength('dot', 'cat', wl) == 0
    wl = []
    assert sol.ladderLength('dog', 'cat', wl) == 0
    wl = ['dog']
    assert sol.ladderLength('dog', 'dog', wl) == 1
    wl = []
    assert sol.ladderLength('dot', 'dog', wl) == 2


def test_1():
    wl = ['hot', 'dot', 'dog', 'lot', 'log']
    assert sol.ladderLength('hit', 'cog', wl) == 5
