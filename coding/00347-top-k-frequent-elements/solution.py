#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = collections.Counter(nums)
        sorted_pairs = sorted(list(counts.items()), key=lambda p: p[1], reverse=True)
        return [v for v, _ in sorted_pairs[:k]]
