# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'

import numpy as np
from solution import Solution


def median(nums1, nums2):
    nums = sorted(nums1 + nums2)
    _len = len(nums)
    if _len == 0:
        return 0
    if _len % 2 == 0:
        k1 = _len // 2
        k2 = k1 - 1
        return (nums[k1] + nums[k2]) / 2.
    else:
        k = _len // 2
        return float(nums[k])


def test_0():
    sol = Solution()
    nums1 = []
    nums2 = []
    assert sol.findMedianSortedArrays(nums1, nums2) == median(nums1, nums2)
    assert sol.findMedianSortedArrays(nums2, nums1) == median(nums1, nums2)


def test_1():
    sol = Solution()
    nums1 = [1, 3, 5, 6, 8]
    nums2 = [2, 3, 4, 5, 6, 7, 8, 9]
    assert sol.findMedianSortedArrays(nums1, nums2) == median(nums1, nums2)
    assert sol.findMedianSortedArrays(nums2, nums1) == median(nums1, nums2)


def test_2():
    sol = Solution()
    nums1 = sorted(np.random.choice(1000, 800, replace=True).tolist())
    nums2 = sorted(np.random.choice(1000, 801, replace=True).tolist())
    assert sol.findMedianSortedArrays(nums1, nums2) == median(nums1, nums2)
    assert sol.findMedianSortedArrays(nums2, nums1) == median(nums1, nums2)


def test_3():
    sol = Solution()
    nums1 = sorted(np.random.choice(1000, 800, replace=True).tolist())
    nums2 = sorted(np.random.choice(1000, 800, replace=True).tolist())
    assert sol.findMedianSortedArrays(nums1, nums2) == median(nums1, nums2)
    assert sol.findMedianSortedArrays(nums2, nums1) == median(nums1, nums2)


def test_4():
    sol = Solution()
    nums1 = sorted(np.random.choice(1000, 801, replace=True).tolist())
    nums2 = sorted(np.random.choice(1000, 801, replace=True).tolist())
    assert sol.findMedianSortedArrays(nums1, nums2) == median(nums1, nums2)
    assert sol.findMedianSortedArrays(nums2, nums1) == median(nums1, nums2)


def test_5():
    sol = Solution()
    nums1 = []
    nums2 = sorted(np.random.choice(1000, 800, replace=True).tolist())
    assert sol.findMedianSortedArrays(nums1, nums2) == median(nums1, nums2)
    assert sol.findMedianSortedArrays(nums2, nums1) == median(nums1, nums2)


def test_6():
    sol = Solution()
    nums1 = range(0, 10)
    nums2 = range(200, 300)
    assert sol.findMedianSortedArrays(nums1, nums2) == median(nums1, nums2)
    assert sol.findMedianSortedArrays(nums2, nums1) == median(nums1, nums2)


def test_7():
    sol = Solution()
    nums1 = [1]
    nums2 = [2, 3, 4, 5, 6, 7]
    assert sol.findMedianSortedArrays(nums1, nums2) == median(nums1, nums2)
    assert sol.findMedianSortedArrays(nums2, nums1) == median(nums1, nums2)


def test_8():
    sol = Solution()
    nums1 = [10, 20, 30, 50, 60, 70, 80]
    nums2 = [9, 11, 23, 35, 43, 49, 51, 63]
    assert sol.findMedianSortedArrays(nums1, nums2) == median(nums1, nums2)
    assert sol.findMedianSortedArrays(nums2, nums1) == median(nums1, nums2)
