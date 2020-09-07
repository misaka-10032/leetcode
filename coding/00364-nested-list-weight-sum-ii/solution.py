#!/usr/bin/env python3
# encoding: utf-8

from typing import List


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
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
    def depthSumInverse(self, nestedList: List['NestedInteger']) -> int:
        def _depth_sum(nested_list: List['NestedInteger'], depth: int,
                       max_depth: List[int], flat_tot: List[int], tot: List[int]):
            for ni in nested_list:
                if ni.isInteger():
                    val = ni.getInteger()
                    weight = max_depth[0] - depth + 1
                    if weight <= 0:
                        delta = depth - max_depth[0]
                        tot[0] += delta * flat_tot[0]
                        max_depth[0] = depth
                        weight = 1
                    flat_tot[0] += val
                    tot[0] += weight * val
                else:
                    _depth_sum(ni.getList(), depth+1, max_depth, flat_tot, tot)
        max_depth = [1]
        flat_tot = [0]
        tot = [0]
        _depth_sum(nestedList, 1, max_depth, flat_tot, tot)
        return tot[0]
