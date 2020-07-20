#!/usr/bin/env python3
# encoding: utf-8

from typing import List


# The read4 API is already defined for you.
def read4(buf4: List[str]) -> int:
    pass


class Solution:
    def __init__(self):
        self._buf = [None] * 4
        self._start = 0
        self._end = 0

    def _maybe_read4(self):
        if self._start == self._end:
            self._start = 0
            self._end = read4(self._buf)

    def _read_local(self, buf: List[str], start: int, n: int) -> int:
        safe_n = min(self._end - self._start, n)
        buf[start:start+safe_n] = self._buf[self._start:self._start+safe_n]
        self._start += safe_n
        return safe_n

    def read(self, buf: List[str], n: int) -> int:
        cnt = 0
        rest = n
        while rest > 0:
            self._maybe_read4()
            local_cnt = self._read_local(buf, cnt, rest)
            if local_cnt == 0:
                return cnt
            cnt += local_cnt
            rest -= local_cnt
        return cnt
