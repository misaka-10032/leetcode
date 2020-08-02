#!/usr/bin/env python3
# encoding: utf-8


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        for pivot in range(n):
            # Case 1: single pivot
            max_wing = min(pivot, n-1-pivot)
            for wing in range(max_wing+1):
                if s[pivot-wing] == s[pivot+wing]:
                    cnt += 1
                else:
                    break
            # Case 2: double pivots
            max_wing = min(pivot, n-2-pivot)
            for wing in range(max_wing+1):
                if s[pivot-wing] == s[pivot+1+wing]:
                    cnt += 1
                else:
                    break
        return cnt
