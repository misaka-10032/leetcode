# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* deque
* sum
* cnt
"""

from collections import deque


class MovingAverage(object):
    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.size = size
        self.sum = 0
        self.cnt = 0
        self.queue = deque()

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.sum += val
        self.cnt += 1
        self.queue.append(val)

        if self.cnt > self.size:
            x = self.queue.popleft()
            self.cnt -= 1
            self.sum -= x

        return float(self.sum) / self.cnt
