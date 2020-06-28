# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import heapq


class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        if not nums1 or not nums2 or k == 0:
            return []

        m = len(nums1)
        n = len(nums2)
        res = []
        heap = []
        pos = [0] * m
        for i in xrange(m):
            heapq.heappush(heap, (nums1[i]+nums2[0], i, 0))

        for _ in xrange(k):
            if not heap:
                break
            s, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]])
            j += 1
            pos[i] = j
            if j < n:
                heapq.heappush(heap, (nums1[i]+nums2[j], i, j))
        return res
