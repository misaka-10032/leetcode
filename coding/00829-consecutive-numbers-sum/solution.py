#!/usr/bin/env python3
# encoding: utf-8


class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        cnt = 0
        n = 1
        while True:
            residual = N - (n - 1) * n // 2
            if residual <= 0:
                break
            if residual % n == 0:
                cnt += 1
            n += 1
        return cnt
