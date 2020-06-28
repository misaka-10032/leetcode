# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import ValidWordAbbr


def test_0():
    sol = ValidWordAbbr([])
    assert sol.isUnique('abc')
    assert sol.isUnique('bcd')


def test_1():
    sol = ValidWordAbbr(['deer', 'door', 'cake', 'card'])
    assert not sol.isUnique('dear')
    assert sol.isUnique('cart')
    assert not sol.isUnique('cane')
    assert sol.isUnique('make')
