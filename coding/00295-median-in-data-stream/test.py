# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import MedianFinder


def test_0():
    mf = MedianFinder()
    assert mf.findMedian() == 0


def test_1():
    mf = MedianFinder()
    arr = []
    for _ in xrange(100):
        x = np.random.randint(-100, 100)
        mf.addNum(x)
        arr.append(x)
        assert mf.findMedian() == np.median(np.array(arr))
