# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_1():
    sol = Solution()
    candidates, target = [2, 3, 6, 7], 7
    key = [[7], [2, 2, 3]]
    ans = sol.combinationSum(candidates, target)
    assert sorted(key) == sorted(ans)


def test_2():
    sol = Solution()
    candidates, target = [3, 6, 9], 7
    key = []
    ans = sol.combinationSum(candidates, target)
    assert sorted(key) == sorted(ans)
