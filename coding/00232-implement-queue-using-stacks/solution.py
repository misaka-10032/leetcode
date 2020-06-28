# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.s_in = deque()
        self.s_out = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.s_in.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        if self.s_out:
            self.s_out.pop()
            return
        while self.s_in:
            self.s_out.append(self.s_in.pop())
        self.s_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.s_out:
            return self.s_out[-1]
        while self.s_in:
            self.s_out.append(self.s_in.pop())
        return self.s_out[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return not(self.s_in or self.s_out)
