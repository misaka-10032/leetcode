# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Codec
cc = Codec()


def _test(strs):
    return cc.decode(cc.encode(strs)) == strs


def test_0():
    assert _test([])
    assert _test(['a'])
    assert _test([' '])
    assert _test(['a b ', ' a b', 'cde gg'])
