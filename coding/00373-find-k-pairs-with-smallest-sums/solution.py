#!/usr/bin/env python3
# encoding: utf-8

import heapq
from typing import List


class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2:
            return []

        swapped = False
        if len(nums1) < len(nums2):
            nums1, nums2 = nums2, nums1
            swapped = True

        # Start by fixing the first element in `nums1`, and push all the candidate pairs
        # by iterating `nums2` to a heap. The element will be (sum, idx1, idx2). We get the result
        # by popping from the heap. When we pop, we see if we can proceed with idx1+1, if so,
        # we need to push (sum, idx1+1, idx2) for the next iteration.
        heap = []
        i1, v1 = 0, nums1[0]
        for i2, v2 in enumerate(nums2):
            heap.append((v1 + v2, i1, i2))
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            if not heap:
                break
            s, i1, i2 = heapq.heappop(heap)
            result.append([nums2[i2], nums1[i1]] if swapped else [nums1[i1], nums2[i2]])
            if i1 + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i1 + 1] + nums2[i2], i1 + 1, i2))
        return result
