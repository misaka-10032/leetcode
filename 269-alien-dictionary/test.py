# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.alienOrder([]) == ''
    assert sol.alienOrder(['']) == ''
    assert sol.alienOrder(['a']) == 'a'


def test_1():
    words = ['wrt', 'wrf', 'er', 'ett', 'rftt']
    assert sol.alienOrder(words) == 'wertf'


def test_2():
    words = ['wrtkj', 'wrt']
    assert sol.alienOrder(words) == ''


def test_3():
    words = ['abc', 'abd', 'ac', 'acd', 'bd']
    assert sol.alienOrder(words) == 'abcd'


def test_4():
    words = ['z', 'z']
    assert sol.alienOrder(words) == 'z'
