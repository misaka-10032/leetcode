# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
class NestedInteger(object):
    def __init__(self, val):
        self.val = val

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        return isinstance(self.val, (int, long))

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        if self.isInteger():
            return self.val
        else:
            return None

    def getList(self):
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        if self.isInteger():
            return None
        else:
            return self.val

    def __repr__(self):
        return str(self.val)


class NestedIterator(object):
    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.G = self._traverse(nestedList)
        self.cache = self.ahead = None
        self.next()

    def _traverse(self, nl):
        for ni in nl:
            if ni.isInteger():
                yield ni.getInteger()
            else:
                for nested in self._traverse(ni.getList()):
                    yield nested

    def next(self):
        """
        :rtype: int
        """
        self.cache = self.ahead
        try:
            self.ahead = self.G.next()
        except StopIteration:
            self.ahead = None
        return self.cache

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ahead is not None


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
