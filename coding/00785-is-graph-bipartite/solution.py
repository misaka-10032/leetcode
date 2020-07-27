#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Set


class Solution:
    def _traverse(self, graph: List[List[int]], u: int, in_s_set: bool,
                  s_set: Set[int], t_set: Set[int]):
        if u in s_set:
            return in_s_set
        if u in t_set:
            return not in_s_set
        # Now we know s is not in either set yet, and we know where to put.
        if in_s_set:
            s_set.add(u)
        else:
            t_set.add(u)
        for v in graph[u]:
            valid = self._traverse(graph, v, not in_s_set, s_set, t_set)
            if not valid:
                return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        s_set, t_set = set(), set()
        n = len(graph)
        for s in range(n):
            if s not in s_set and s not in t_set:
                valid = self._traverse(graph, s, True, s_set, t_set)
                if not valid:
                    return False
        return True
