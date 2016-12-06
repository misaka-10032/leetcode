# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from solution import Solution
sol = Solution()


def test_0():
    assert not sol.containsNearbyDuplicate([], 1)
    assert not sol.containsNearbyDuplicate([1], 1)
    assert sol.containsNearbyDuplicate([1, 1], 1)
    assert not sol.containsNearbyDuplicate([1, 2, 1], 1)
    assert sol.containsNearbyDuplicate([1, 2, 1], 2)
    assert sol.containsNearbyDuplicate([1, 2, 3, 2, 4], 2)
    assert not sol.containsNearbyDuplicate([1, 2, 3, 4, 2], 2)
