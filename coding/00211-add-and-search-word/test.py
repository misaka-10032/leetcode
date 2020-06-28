# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import WordDictionary


def test_0():
    t = WordDictionary()
    assert not t.search('.')
    assert not t.search('a')
    t.addWord('a')
    assert t.search('.')
    assert t.search('a')


def test_1():
    t = WordDictionary()
    t.addWord("bad")
    t.addWord("dad")
    t.addWord("mad")
    assert not t.search("pad")
    assert t.search("bad")
    assert t.search(".ad")
    assert t.search("b..")
