# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def ref(a, b):
    return '{:b}'.format(int(a, 2) + int(b, 2))


def test_0():
    assert sol.addBinary('0', '0') == ref('0', '0')
    assert sol.addBinary('111', '0') == ref('111', '0')
    assert sol.addBinary('0', '111') == ref('0', '111')
    assert sol.addBinary('1', '1') == ref('1', '1')


def test_1():
    for a in xrange(100):
        for b in xrange(100):
            sa = '{:b}'.format(a)
            sb = '{:b}'.format(b)
            assert sol.addBinary(sa, sb) == ref(sa, sb)
