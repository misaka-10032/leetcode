# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import MinStack


def test():
    s = MinStack()
    s.push(2)
    assert s.top() == 2
    assert s.getMin() == 2
    s.push(3)
    assert s.top() == 3
    assert s.getMin() == 2
    s.pop()
    assert s.top() == 2
    assert s.getMin() == 2
    s.push(4)
    s.push(5)
    assert s.top() == 5
    assert s.getMin() == 2
    s.push(1)
    assert s.top() == 1
    assert s.getMin() == 1
    s.push(2)
    assert s.top() == 2
    assert s.getMin() == 1
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.pop()
    s.push(5)
    assert s.top() == 5
    assert s.getMin() == 5
