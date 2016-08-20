# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import heapq


class MedianFinder:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.H_max = []
        self.H_min = []

    def addNum(self, num):
        """
        Adds a num into the data structure.
        :type num: int
        :rtype: void
        """
        if num < self.findMedian():
            heapq.heappush(self.H_max, -num)
        else:
            heapq.heappush(self.H_min, num)
        if len(self.H_max) - len(self.H_min) > 1:
            x = -heapq.heappop(self.H_max)
            heapq.heappush(self.H_min, x)
        elif len(self.H_min) - len(self.H_max) > 1:
            x = heapq.heappop(self.H_min)
            heapq.heappush(self.H_max, -x)

    def findMedian(self):
        """
        Returns the median of current data stream
        :rtype: float
        """
        if not self.H_min and not self.H_max:
            return 0
        if len(self.H_min) < len(self.H_max):
            return -self.H_max[0]
        if len(self.H_min) > len(self.H_max):
            return self.H_min[0]
        return (self.H_min[0]-self.H_max[0]) / 2.


# Your MedianFinder object will be instantiated and called as such:
# mf = MedianFinder()
# mf.addNum(1)
# mf.findMedian()
