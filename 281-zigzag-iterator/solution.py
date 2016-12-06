# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class ZigzagIterator(object):
    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.vals = [v1, v2]
        self.ids = [0, 0]
        self.which = 1

    def next(self):
        """
        :rtype: int
        """
        self.which = not self.which
        v = self.vals[self.which]
        i = self.ids[self.which]
        if i < len(v):
            r = v[i]
            self.ids[self.which] += 1
            return r
        return self.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ids[0] != len(self.vals[0]) or \
               self.ids[1] != len(self.vals[1])
