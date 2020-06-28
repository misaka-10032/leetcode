# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import NestedInteger, NestedIterator


def test_0():
    it = NestedIterator([])
    assert not it.hasNext()

    it = NestedIterator([NestedInteger(1)])
    assert it.hasNext()
    assert it.next() == 1
    assert not it.hasNext()

    it = NestedIterator([NestedInteger([NestedInteger([NestedInteger(1)])])])
    assert it.hasNext()
    assert it.next() == 1
    assert not it.hasNext()


def test_1():
    it = NestedIterator([NestedInteger([NestedInteger(1), NestedInteger(1)]),
                         NestedInteger(2),
                         NestedInteger([NestedInteger(1),
                                        NestedInteger([NestedInteger(4),
                                                       NestedInteger(6)])]),
                         NestedInteger(9)])
    res = []
    while it.hasNext():
        res.append(it.next())
    assert res == [1, 1, 2, 1, 4, 6, 9]
