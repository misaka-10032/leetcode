# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

It's actually the reverse topological order. Maintain

* remained
* heads
* inlinks
* outlinks
* order

"""

from collections import defaultdict


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        remained = set(xrange(numCourses))
        outlinks = defaultdict(set)
        inlinks = defaultdict(set)
        for c1, c2 in prerequisites:
            outlinks[c1].add(c2)
            inlinks[c2].add(c1)

        heads = set()
        for c in remained:
            if not inlinks[c]:
                heads.add(c)

        order = []
        while heads:
            u = heads.pop()
            order.append(u)
            remained.remove(u)
            for v in outlinks[u]:
                inlinks[v].remove(u)
                if not inlinks[v]:
                    heads.add(v)
                    del inlinks[v]
            del outlinks[u]

        # unresolved dependencies
        if remained:
            return []

        return order[::-1]
