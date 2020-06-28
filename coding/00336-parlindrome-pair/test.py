# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test1():
    sol = Solution()
    ans = sol.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"])
    assert sorted(ans) == sorted([[0, 1], [1, 0], [3, 2], [2, 4]])


def test2():
    sol = Solution()
    ans = sol.palindromePairs(["abcba", ""])
    assert sorted(ans) == sorted([[0, 1], [1, 0]])


def test3():
    sol = Solution()
    ans = sol.palindromePairs(["aaa", "aa"])
    assert sorted(ans) == sorted([[0, 1], [1, 0]])
