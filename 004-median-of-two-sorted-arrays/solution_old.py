# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

Binary search.
"""
__author__ = 'misaka-10032'


class Solution(object):
    def first_ge(self, x, nums, p, q):
        """
        Find the first num >= x within nums[p:q].
        Find a lower bound.
        :param x:
        :param nums: sorted list
        :param p:
        :param q:
        :return: idx
        """
        assert p < q
        r, t = p, q
        while r < t:
            m = (r + t) // 2
            if x > nums[m]:
                r = m + 1
            elif x < nums[m]:
                t = m
            else:
                return self.leftmost(m, nums, p, q)
        """ Can either be r == m == t or m <= r == t """
        return r

    def first_gt(self, x, nums, p, q):
        """
        Find the first num > x within nums[p:q].
        Find an upper bound.
        :param x:
        :param nums:
        :param p:
        :param q:
        :return: idx
        """
        assert p < q
        r, t = p, q
        while r < t:
            m = (r + t) // 2
            if x > nums[m]:
                r = m + 1
            elif x < nums[m]:
                t = m
            else:
                return self.rightmost(m, nums, p, q) + 1
        """  Can either be r == m == t or m <= r == t """
        return r

    def leftmost(self, idx, nums, p, q):
        """
        Given idx, find leftmost idx i1 within nums[p:q),
        such that nums[i1] = nums[idx].
        :param idx:
        :param nums:
        :param p:
        :param q:
        :return:
        """
        x = nums[idx]
        while idx >= p and nums[idx] == x:
            idx -= 1
        return idx + 1

    def rightmost(self, idx, nums, p, q):
        x = nums[idx]
        while idx < q and nums[idx] == x:
            idx += 1
        return idx - 1

    def _find_kth(self, k, nums1, nums2):
        """
        Try to find kth within nums1[p1:q1].
        :param k:
        :param nums1:
        :param nums2:
        :return: kth smallest number. None if not found.
        """
        p1, q1 = 0, len(nums1)
        p2, q2 = 0, len(nums2)
        """ Search within nums1. """
        while p1 < q1:
            m1 = (p1 + q1) // 2
            x = nums1[m1]
            r1 = self.leftmost(m1, nums1, p1, q1)
            r2 = self.first_ge(x, nums2, p2, q2)
            r = r1 + r2
            t1 = self.rightmost(m1, nums1, p1, q1)
            t2 = self.first_gt(x, nums2, p2, q2)
            t = t1 + t2
            """ x \in [r, t] """
            if k < r:
                q1 = r1
                """ In this case x_ge needs to be included, because
                in the next round x' < x <= x_ge, this x_ge would still be a bound.
                """
                """ Tricky: to not only stay in bound, but also include x_ge """
                q2 = r2 + 1 if r2 < q2 else q2
            elif k > t:
                p1 = t1 + 1
                """ In this case x+ needs to be included, because
                in the next round x_le <= x < x' <= x'_ge, x_le is no longer useful,
                but x_gt may still be a bound.
                """
                """ Tricky: x_gt not exist, stay back. """
                p2 = t2 if t2 < q2 else t2 - 1
            else:
                return x
        return None

    def median(self, nums):
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

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if not nums1 and not nums2:
            return 0
        if not nums1:
            return self.median(nums2)
        if not nums2:
            return self.median(nums1)

        len1 = len(nums1)
        len2 = len(nums2)
        _len = len1 + len2
        if _len % 2 != 0:
            k = _len // 2
            x = self._find_kth(k, nums1, nums2)
            x = x if x else self._find_kth(k, nums2, nums1)
            return float(x)
        else:
            k1 = _len // 2
            x1 = self._find_kth(k1, nums1, nums2)
            x1 = x1 if x1 else self._find_kth(k1, nums2, nums1)
            k2 = k1 - 1
            x2 = self._find_kth(k2, nums1, nums2)
            x2 = x2 if x2 else self._find_kth(k2, nums2, nums1)
            return (x1 + x2) / 2.
