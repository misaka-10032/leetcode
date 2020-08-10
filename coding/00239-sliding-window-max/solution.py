#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import List


class DecreasingGarbageCollectionQueue:
    def __init__(self, ttl: int):
        self._ttl = ttl
        self._q = collections.deque()

    def append(self, t: int, v: int):
        # First, clean up the stale elements.
        while self._q and self._q[0][0] + self._ttl <= t:
            self._q.popleft()
        # Second, make sure the values are decreasing.
        while self._q and self._q[-1][1] <= v:
            self._q.pop()
        self._q.append((t, v))

    def peek(self) -> int:
        return self._q[0][1]


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Construct a queue that has decreasing values, and only contains the
        # element in a time window.
        q = DecreasingGarbageCollectionQueue(k)
        result = []
        for i, v in enumerate(nums):
            q.append(i, v)
            if i < k - 1:
                continue
            result.append(q.peek())
        return result
