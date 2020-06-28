# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    nums = [0, 1, 3, 50, 75]
    tgt = ["2", "4->49", "51->74", "76->99"]
    assert sol.findMissingRanges(nums, 0, 99) == tgt


def test_1():
    nums = [0, 1, 3, 50, 75]
    tgt = ["2", "4->49", "51->74"]
    assert sol.findMissingRanges(nums, 0, 75) == tgt


def test_2():
    nums = [0, 1, 3, 50, 75]
    tgt = ["-1", "2", "4->49", "51->74"]
    assert sol.findMissingRanges(nums, -1, 75) == tgt


def test_3():
    nums = [0, 1, 3, 50, 75]
    tgt = ["-3->-1", "2", "4->49", "51->74"]
    assert sol.findMissingRanges(nums, -3, 75) == tgt
