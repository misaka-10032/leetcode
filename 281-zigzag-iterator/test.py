# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import ZigzagIterator


def traverse(it):
    r = []
    while it.hasNext():
        r.append(it.next())
    return r


def test_0():
    it = ZigzagIterator([], [])
    assert not it.hasNext()

    it = ZigzagIterator([1], [])
    assert it.hasNext()
    assert it.next() == 1
    assert not it.hasNext()

    it = ZigzagIterator([], [1])
    assert it.hasNext()
    assert it.next() == 1
    assert not it.hasNext()


def test_1():
    it = ZigzagIterator([1, 2], [3, 4, 5, 6])
    r = traverse(it)
    assert r == [1, 3, 2, 4, 5, 6]
