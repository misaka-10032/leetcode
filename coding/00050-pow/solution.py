#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def _to_binary(self, n: int) -> List[int]:
        result = []
        while n > 0:
            result.append(n % 2)
            n >>= 1
        return result

    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1.

        powers = []
        vals = []
        power = 1
        val = x
        while power <= abs(n):
            powers.append(power)
            vals.append(val)
            power <<= 1
            val *= val

        binary_n = self._to_binary(abs(n))
        result = 1.
        for idx, bit in enumerate(binary_n):
            if bit:
                result *= vals[idx]
        return result if n > 0 else 1. / result
