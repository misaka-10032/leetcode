# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test():
    sol = Solution()
    assert sol.numTrees(1) == 1
    assert sol.numTrees(3) == 5
