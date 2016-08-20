# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

This is a super SILLY problem
"""

from collections import deque


class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.Q = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        old_len = len(self.Q)
        self.Q.append(x)
        for _ in xrange(old_len):
            self.Q.append(self.Q.popleft())

    def pop(self):
        """
        :rtype: nothing
        """
        self.Q.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.Q[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.Q
