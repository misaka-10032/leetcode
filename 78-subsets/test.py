# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.subsets([]) == [[]]
    assert sorted(sol.subsets([10])) == sorted([[], [10]])


def test_1():
    sol = Solution()
    nums = [1, 2, 3]
    ans = [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(sol.subsets(nums)) == sorted(ans)
