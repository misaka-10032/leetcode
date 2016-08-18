# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import NumArray


def test_0():
    nums = NumArray([2])
    assert nums.sumRange(0, 0) == 2


def test_1():
    nums = NumArray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    assert nums.sumRange(0, 0) == 0
    assert nums.sumRange(9, 9) == 9
    assert nums.sumRange(0, 9) == 45
    assert nums.sumRange(2, 3) == 5


def test_2():
    nums = NumArray([1, 3, 5])
    assert nums.sumRange(0, 2) == 9
    nums.update(1, 2)
    assert nums.sumRange(0, 2) == 8
