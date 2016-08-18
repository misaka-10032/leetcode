# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution


def test_0():
    sol = Solution()
    nums, k, t = [], 1, 1
    assert not sol.containsNearbyAlmostDuplicate(nums, k, t)
    nums, k, t = [1], 1, 1
    assert not sol.containsNearbyAlmostDuplicate(nums, k, t)
    nums, k, t = [1, 1], 1, 0
    assert sol.containsNearbyAlmostDuplicate(nums, k, t)
    nums, k, t = [1, 2], 1, 0
    assert not sol.containsNearbyAlmostDuplicate(nums, k, t)


def test_1():
    sol = Solution()
    nums, k, t = [1, 1, 2, 3], 3, 1
    assert sol.containsNearbyAlmostDuplicate(nums, k, t)
    nums, k, t = [9, 5, 1, 3, 6, 9], 1, 2
    assert sol.containsNearbyAlmostDuplicate(nums, k, t)
    nums, k, t = [9, 5, 1, 3, 6, 9], 1, 1
    assert not sol.containsNearbyAlmostDuplicate(nums, k, t)
