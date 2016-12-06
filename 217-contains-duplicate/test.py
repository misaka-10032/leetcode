# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert not sol.containsDuplicate([])
    assert not sol.containsDuplicate([1])
    assert sol.containsDuplicate([1, 1])
