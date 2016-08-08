# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


# def test_0():
#     sol = Solution()
#     assert sol.searchInsert([], 1) == 0
#     assert sol.searchInsert([2], 1) == 0
#     assert sol.searchInsert([2], 2) == 0
#     assert sol.searchInsert([2], 3) == 1


def test_1():
    sol = Solution()
    # assert sol.searchInsert([1, 3, 5, 6, 7, 9], 5) == 2
    # assert sol.searchInsert([1, 3, 5, 6, 7, 9], 2) == 1
    # assert sol.searchInsert([1, 3, 5, 6, 7, 9], 7) == 4
    # assert sol.searchInsert([1, 3, 5, 6, 7, 9], 9) == 5
    # assert sol.searchInsert([1, 3, 5, 6, 7, 9], 10) == 6
    assert sol.searchInsert([1, 3, 5, 6, 7, 9], 0) == 0
