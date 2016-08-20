# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import RandomizedCollection


def test_1():
    s = RandomizedCollection()
    assert s.insert(1)
    assert s.getRandom() == 1
    assert s.insert(2)
    assert s.insert(3)
    assert s.remove(1)
    assert s.remove(2)
    assert s.getRandom() == 3
    assert s.remove(3)
    assert s.insert(1)
    assert s.getRandom() == 1


def test_2():
    s = RandomizedCollection()
    assert s.insert(1)
    assert not s.insert(1)
    assert not s.insert(1)
    assert s.getRandom() == 1
    assert s.insert(2)
    assert not s.insert(2)
    assert s.insert(3)
    assert s.remove(1)
    assert s.remove(1)
    assert s.remove(1)
    assert s.remove(2)
    assert s.remove(2)
    assert s.getRandom() == 3
    assert s.remove(3)
    assert s.insert(1)
    assert s.getRandom() == 1
