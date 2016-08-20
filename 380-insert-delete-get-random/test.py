# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import RandomizedSet


def test_1():
    s = RandomizedSet()
    assert s.insert(1)
    assert s.getRandom() == 1
    assert s.insert(2)
    assert not s.insert(2)
    assert s.insert(3)
    assert s.remove(1)
    assert s.remove(2)
    assert s.getRandom() == 3
    assert s.remove(3)
    assert s.insert(1)
    assert s.getRandom() == 1
