#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        cand_counts = sorted(
            collections.Counter(candidates).items(),
            key=lambda p: -p[0])
        # sums[i] tracks the sum of cand_counts[i+1:]
        sums = [0] * len(cand_counts)
        for i in range(len(sums) - 2, -1, -1):
            sums[i] = sums[i + 1] + cand_counts[i + 1][0] * cand_counts[i + 1][1]

        result = []

        def _search(idx: int, comb_sum: int, comb: List[int]):
            if comb_sum == target:
                result.append(comb[:])
                return
            if idx == len(cand_counts):
                return
            cand, count = cand_counts[idx]
            actual_count = 0
            while True:
                if comb_sum + sums[idx] >= target:
                    _search(idx + 1, comb_sum, comb)
                if actual_count == count:
                    break
                if comb_sum + cand > target:
                    break
                actual_count += 1
                comb.append(cand)
                comb_sum += cand
            for _ in range(actual_count):
                comb.pop()
            comb_sum -= cand * actual_count

        _search(0, 0, [])
        return result
