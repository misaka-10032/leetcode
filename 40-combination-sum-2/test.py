# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_1():
    sol = Solution()
    candidates, target = [10, 1, 2, 7, 6, 1, 5], 8
    key = [[1, 7], [1, 2, 5], [2, 6], [1, 1, 6]]
    ans = sol.combinationSum2(candidates, target)
    assert sorted(key) == sorted(ans)


def test_2():
    sol = Solution()
    candidates, target = [2, 2, 2], 2
    key = [[2]]
    ans = sol.combinationSum2(candidates, target)
    assert sorted(key) == sorted(ans)
