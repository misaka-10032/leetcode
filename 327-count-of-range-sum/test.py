# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import numpy as np
from solution import Solution


def test_0():
    sol = Solution()
    assert sol.countRangeSum([], 2, 4) == 0
    assert sol.countRangeSum([1], 2, 4) == 0
    assert sol.countRangeSum([2], 2, 4) == 1
    assert sol.countRangeSum([3], 2, 4) == 1
    assert sol.countRangeSum([4], 2, 4) == 1
    assert sol.countRangeSum([5], 2, 4) == 0


def test_1():
    sol = Solution()
    for _ in xrange(10):
        nums = np.random.randint(-100, 100, 100).tolist()
        lower, upper = sorted(np.random.randint(-100, 100, 2))
        prefix = list(nums)
        for i in xrange(1, len(prefix)):
            prefix[i] += prefix[i-1]
        cnt = 0
        for i in xrange(len(prefix)):
            left = prefix[i-1] if i > 0 else 0
            for j in xrange(i, len(prefix)):
                if lower <= prefix[j] - left <= upper:
                    cnt += 1
        assert cnt == sol.countRangeSum(nums, lower, upper)
