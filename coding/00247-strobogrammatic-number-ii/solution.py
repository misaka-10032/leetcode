#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:
        if n <= 0:
            return [""]

        rotation_map = {
            '0': '0',
            '1': '1',
            '6': '9',
            '8': '8',
            '9': '6',
        }

        result = []

        def _search(i: int, curr: List[str]):
            if i == (n + 1) // 2:
                result.append(''.join(curr))
                return

            for c, rc in rotation_map.items():
                if i == n // 2 and n % 2 == 1 and c != rc:
                    continue
                if i == 0 and n > 1 and c == '0':
                    continue
                curr[i] = c
                curr[n - 1 - i] = rc
                _search(i + 1, curr)
                curr[i] = curr[n - 1 - i] = ''

        _search(0, [''] * n)
        return result
