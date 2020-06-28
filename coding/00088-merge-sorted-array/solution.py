# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = m-1
        j = n-1
        k = -1
        for k in xrange(m+n-1, -1, -1):
            if i < 0 or j < 0:
                break
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
        if i < 0:
            nums1[k::-1] = nums2[j::-1]
        # when j < 0, what's left in nums1 is already done.
