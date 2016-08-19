# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import LRUCache


def test_0():
    lru = LRUCache(0)
    for _ in xrange(10):
        k, v = np.random.randint(-100, 100, 2)
        lru.set(k, v)
        assert lru.get(k) == -1


def test_1():
    lru = LRUCache(1)
    k_prev = np.random.randint(-100, 100)
    for _ in xrange(10):
        k, v = np.random.randint(-100, 100, 2)
        lru.set(k, v)
        assert lru.get(k) == v
        assert lru.get(k_prev) == -1
        k_prev = k


def test_2():
    lru = LRUCache(2)
    assert lru.get(2) == -1
    lru.set(1, 1)
    assert lru.get(1) == 1
    lru.set(2, 2)
    lru.set(3, 3)
    assert lru.get(1) == -1
    assert lru.get(2) == 2
    lru.set(4, 4)
    assert lru.get(3) == -1
    assert lru.get(2) == 2
    assert lru.get(4) == 4


def test_3():
    lru = LRUCache(3)
    assert lru.get(3) == -1
    lru.set(1, 1)
    lru.set(2, 2)
    lru.set(3, 3)
    lru.set(4, 4)
    assert lru.get(1) == -1
    assert lru.get(2) == 2
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    lru.set(5, 5)
    assert lru.get(2) == -1
    assert lru.get(3) == 3
    assert lru.get(4) == 4
    assert lru.get(5) == 5


def test_4():
    lru = LRUCache(2)
    lru.set(2, 1)
    lru.set(2, 2)
    assert lru.get(2) == 2
    lru.set(1, 1)
    lru.set(4, 1)
    assert lru.get(2) == -1


def test_5():
    lru = LRUCache(2)
    lru.set(1, 1)
    lru.set(2, 2)
    assert lru.get(2) == 2
    lru.set(3, 3)
    assert lru.get(1) == -1
    assert lru.get(2) == 2
    assert lru.get(3) == 3
