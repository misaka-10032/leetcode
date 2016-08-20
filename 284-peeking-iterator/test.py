# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import PeekingIterator, Iterator


def test_0():
    it = PeekingIterator(Iterator([]))
    assert not it.hasNext()


def test_1():
    it = PeekingIterator(Iterator([1, 2, 3, 4]))
    res = []
    while it.hasNext():
        res.append(it.peek())
        res.append(it.next())
    assert res == [1, 1, 2, 2, 3, 3, 4, 4]
