#!/usr/bin/env python3
# encoding: utf-8


from typing import Dict, Tuple

_MOD = (10 ** 9) + 7
_NEXT = (
    (4, 6),  # 0
    (6, 8),  # 1
    (7, 9),  # 2
    (4, 8),  # 3
    (0, 3, 9),  # 4
    None,  # 5
    (0, 1, 7),  # 6
    (2, 6),  # 7
    (1, 3),  # 8
    (2, 4),  # 9
)


class Solution:
    def _search(self, curr: int, steps: int,
                cache: Dict[Tuple[int, int], int]) -> int:
        if steps == 0:
            return 1
        if curr == 5:
            return 0

        maybe_result = cache.get((curr, steps), None)
        if maybe_result is not None:
            return maybe_result

        cnt = 0
        for next_digit in _NEXT[curr]:
            cnt += self._search(next_digit, steps - 1, cache)
        cache[(curr, steps)] = cnt
        return cnt % _MOD

    def knightDialer(self, N: int) -> int:
        cnt = 0
        cache = {}
        for i in range(10):
            cnt += self._search(i, N - 1, cache)
        return cnt % _MOD
