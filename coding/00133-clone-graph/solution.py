# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Definition for a undirected graph node
class UndirectedGraphNode(object):
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution(object):
    def _clone(self, old, old2new):
        """ d maps old node to new neighbors """
        if old in old2new:
            return old2new[old]
        new = UndirectedGraphNode(old.label)
        new.neighbors = [None] * len(old.neighbors)
        old2new[old] = new
        for i, old_neighbor in enumerate(old.neighbors):
            new_neighbor = self._clone(old_neighbor, old2new)
            new.neighbors[i] = new_neighbor
        return new

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if not node:
            return None
        return self._clone(node, {})
