# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.canFinish(10, [])
    assert sol.canFinish(2, [[1, 0]])
    assert not sol.canFinish(2, [[1, 0], [0, 1]])
