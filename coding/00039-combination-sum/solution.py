#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        cache = {}

        def _search(target: int) -> List[List[int]]:
            result = cache.get(target)
            if result is not None:
                return result

            result = []
            for c in candidates:
                if c > target:
                    continue
                if c == target:
                    result.append([c])
                    continue
                smaller_result = _search(target - c)
                for comb in smaller_result:
                    if c >= comb[-1]:
                        result.append(comb + [c])
            cache[target] = result
            return result

        return _search(target)
