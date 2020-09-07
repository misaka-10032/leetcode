#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def longestOnes(self, A: List[int], K: int) -> int:
        n = len(A)
        left = 0
        right = -1
        budget = K
        max_cnt = 0
        while True:
            right += 1
            if right == n:
                break
            if A[right] == 0:
                budget -= 1
            while budget < 0:
                if A[left] == 0:
                    budget += 1
                left += 1
            max_cnt = max(max_cnt, right-left+1)
        return max_cnt
