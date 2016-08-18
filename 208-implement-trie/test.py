# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Trie


def test_0():
    t = Trie()
    assert not t.search('a')
    assert not t.startsWith('sa')


def test_1():
    t = Trie()
    t.insert('apple')
    t.insert('pear')
    assert t.search('apple')
    assert not t.search('app')
    assert t.startsWith('app')
