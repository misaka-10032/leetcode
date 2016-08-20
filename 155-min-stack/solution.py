# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque

MIN = -999999999


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.S = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        min_ = min(x, self.S[-1][1]) if self.S else x
        self.S.append((x, min_))

    def pop(self):
        """
        :rtype: void
        """
        self.S.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.S[-1][0]

    def getMin(self):
        """
        :rtype: int
        """
        return self.S[-1][1] if self.S else MIN


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()