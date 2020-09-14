#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        rotation_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }

        def _search(i: int, n: int, lo: List[str], hi: List[str],
                    curr_lo: List[str], curr_hi: List[str], cnt: List[int]):
            if i == (n + 1) // 2:
                cnt[0] += 1
                return

            for c, rc in rotation_map.items():
                if i == n // 2 and n % 2 == 1 and c != rc:
                    continue
                if i == 0 and n > 1 and c == '0':
                    continue
                curr_lo[i] = curr_hi[i] = c
                ri = n - 1 - i
                curr_lo[ri] = curr_hi[ri] = rc
                if curr_hi >= lo and curr_lo <= hi:
                    _search(i + 1, n, lo, hi, curr_lo, curr_hi, cnt)
                curr_lo[i] = curr_lo[ri] = '0'
                curr_hi[i] = curr_hi[ri] = '9'

        cnt = [0]
        for n in range(len(low), len(high) + 1):
            if n == len(low):
                lo = list(low)
            else:
                lo = ['1'] + ['0'] * (n - 1)
            if n == len(high):
                hi = list(high)
            else:
                hi = ['9'] * n
            _search(0, n, lo, hi, ['0'] * n, ['9'] * n, cnt)

        return cnt[0]
