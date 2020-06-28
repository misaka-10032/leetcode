# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.fullJustify(['a'], 1) == ['a']
    assert sol.fullJustify(['a'], 2) == ['a ']
    assert sol.fullJustify(['a'], 4) == ['a   ']
    assert sol.fullJustify(['a', 'b'], 4) == ['a b ']


def test_1():
    words = ["This", "is", "an", "example",
             "of", "text", "justification."]
    tgt = ["This    is    an",
           "example  of text",
           "justification.  "]
    assert sol.fullJustify(words, 16) == tgt
