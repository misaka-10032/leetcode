# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert sol.wordsTyping(['a'], 0, 0) == 0
    assert sol.wordsTyping(['a'], 1, 0) == 0
    assert sol.wordsTyping(['a'], 1, 1) == 1


def test_1():
    assert sol.wordsTyping(['hello', 'world'], 2, 8) == 1
    assert sol.wordsTyping(['a', 'bcd', 'e'], 3, 6) == 2
    assert sol.wordsTyping(['i', 'had', 'apple', 'pie'], 4, 5) == 1
