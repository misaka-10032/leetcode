# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* Fix the element in the first array; move the pointer in the second array.
* Each time, we need to pick a candidate from the heap of all possible pairs.

* Heap element would look like (x, i, j), where x is val, i is idx in nums1 and j is idx in nums2.
* pop it, move j forward, and push j+1 if any.

* len(heap) == len(nums1), so make len(nums1) smaller.
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
        if not nums1 or not nums2:
            return []

        exchanged = False
        if len(nums1) > len(nums2):
            exchanged = True
            nums1, nums2 = nums2, nums1

        m = len(nums1)
        n = len(nums2)
        heap = []
        for i in xrange(m):
            heap.append((nums1[i] + nums2[0], i, 0))

        res = []
        for _ in xrange(k):
            if not heap:
                break
            x, i, j = heapq.heappop(heap)
            res.append([nums1[i], nums2[j]] if not exchanged else [nums2[j], nums1[i]])
            j += 1
            if j < n:
                heapq.heappush(heap, (nums1[i] + nums2[j], i, j))
        return res
