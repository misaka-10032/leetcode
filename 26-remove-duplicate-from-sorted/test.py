# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test():
    sol = Solution()
    a = []
    assert sol.removeDuplicates(a) == 0 and a == []
    a = [1]
    assert sol.removeDuplicates(a) == 1 and a[:1] == [1]
    a = [1, 1, 2, 2, 2, 3]
    assert sol.removeDuplicates(a) == 3 and a[:3] == [1, 2, 3]
