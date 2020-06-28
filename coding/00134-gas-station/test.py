# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    assert sol.canCompleteCircuit([], []) == -1
    assert sol.canCompleteCircuit([2], [1]) == 0
    assert sol.canCompleteCircuit([1], [1]) == 0
    assert sol.canCompleteCircuit([1], [2]) == -1


def test_1():
    sol = Solution()
    gas = [5, 0, 0, 0, 0, 0, 3]
    cost = [1, 1, 1, 1, 1, 1, 1]
    assert sol.canCompleteCircuit(gas, cost) == 6


def test_2():
    sol = Solution()
    gas = [5, 0, 0, 0, 0, 0, 2]
    cost = [1, 1, 1, 1, 1, 1, 1]
    assert sol.canCompleteCircuit(gas, cost) == 6


def test_3():
    sol = Solution()
    gas = [5, 0, 0, 0, 0, 0, 1]
    cost = [1, 1, 1, 1, 1, 1, 1]
    assert sol.canCompleteCircuit(gas, cost) == -1
