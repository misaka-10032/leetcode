#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = collections.Counter(nums1)
        counter2 = collections.Counter(nums2)
        if len(counter1) > len(counter2):
            counter1, counter2 = counter2, counter1

        result = []
        for v, cnt1 in counter1.items():
            cnt2 = counter2[v]
            result.extend([v] * min(cnt1, cnt2))
        return result
