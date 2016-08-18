# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    def __eq__(self, other):
        return self.start == other[0] and \
               self.end == other[1]


class Root(object):
    def __init__(self, start, end, rank):
        self.start = start
        self.end = end
        self.rank = rank


class SummaryRanges(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.parents = {}
        self.roots = {}

    def union(self, x, y):
        x_old = x
        while self.parents[x] != x:
            x = self.parents[x]
        self.parents[x_old] = x  # compression

        y_old = y
        while self.parents[y] != y:
            y = self.parents[y]
        self.parents[y_old] = y  # compression

        if self.roots[x].rank < self.roots[y].rank:
            x, y = y, x
        x_root = self.roots[x]
        y_root = self.roots.pop(y)
        self.parents[y] = x
        x_root.rank = max(x_root.rank, 1+y_root.rank)
        x_root.start = min(x_root.start, y_root.start)
        x_root.end = max(x_root.end, y_root.end)

    def addNum(self, val):
        """
        :type val: int
        :rtype: void
        """
        if val in self.parents:
            return
        left = val - 1
        right = val + 1
        self.parents[val] = val
        self.roots[val] = Root(val, val, 0)
        if left in self.parents:
            self.union(left, val)
        if right in self.parents:
            self.union(right, val)

    def getIntervals(self):
        """
        :rtype: List[Interval]
        """
        res = []
        for key in sorted(self.roots.keys()):
            root = self.roots[key]
            res.append(Interval(root.start, root.end))
        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()
