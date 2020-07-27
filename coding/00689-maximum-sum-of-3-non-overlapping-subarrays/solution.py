#!/usr/bin/env python3
# encoding: utf-8


from typing import List


class Solution:

    def _range_sums(self, nums: List[int], k: int) -> List[int]:
        # rsums[i] = sum(nums[i-k:i])
        rsums = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            rsums[i + 1] = rsums[i] + nums[i]
            if i >= k:
                rsums[i + 1] -= nums[i - k]
        return rsums

    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        rsums = self._range_sums(nums, k)
        n = len(nums)
        d = 3  # Number of subarrays
        # f[c][j] means the max sum when we have c subarrays and end at j.
        f = [[0 for _ in range(n + 1)] for _ in range(d + 1)]
        # last[c][j] tracks the last *start* index of f[c][j]
        last = [[-1 for _ in range(n + 1)] for _ in range(d + 1)]
        for c in range(1, d + 1):
            # j starts at c*k because we need to leave space for c ranges.
            # We have (d-c) left, so we need to leave (d-c)*k space at then end.
            for j in range(c * k, n + 1 - (d - c) * k):
                v1 = f[c][j - 1] if j > 1 else 0
                v2 = f[c - 1][j - k] + rsums[j]
                if v1 >= v2:
                    last[c][j] = last[c][j - 1]
                    f[c][j] = v1
                else:
                    last[c][j] = j - k
                    f[c][j] = v2
        inverse_result = [last[d][n]]
        for c in range(d - 1, 0, -1):
            last_idx = inverse_result[-1]
            inverse_result.append(last[c][last_idx])
        return inverse_result[::-1]
