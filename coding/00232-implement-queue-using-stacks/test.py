# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Queue


def test_1():
    q = Queue()
    assert q.empty()
    q.push(1)
    assert q.peek() == 1
    q.push(2)
    assert q.peek() == 1
    q.push(3)
    q.push(4)
    q.pop()
    q.pop()
    q.pop()
    assert q.peek() == 4
    q.pop()
    assert q.empty()
