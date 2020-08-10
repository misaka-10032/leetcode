#!/usr/bin/env python3
# encoding: utf-8

from typing import List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class Solution:
    def _depth_sum(self, ni: NestedInteger, depth: int) -> int:
        if ni.isInteger():
            return ni.getInteger() * depth
        else:
            tot = 0
            for ni2 in ni.getList():
                tot += self._depth_sum(ni2, depth + 1)
            return tot

    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        tot = 0
        for ni in nestedList:
            tot += self._depth_sum(ni, 1)
        return tot
