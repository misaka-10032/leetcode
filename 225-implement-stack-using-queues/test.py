# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Stack


def test_1():
    s = Stack()
    assert s.empty()
    s.push(1)
    assert not s.empty()
    assert s.top() == 1
    s.pop()
    assert s.empty()

    s.push(2)
    assert s.top() == 2
    s.push(3)
    s.push(4)
    s.push(5)
    s.pop()
    assert s.top() == 4
    assert s.top() == 4
    s.pop()
    assert s.top() == 3
    s.pop()
    s.push(6)
    s.push(7)
    s.pop()
    s.pop()
    assert s.top() == 2
    s.pop()
    assert s.empty()
