# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def dfs(self, k):
        self.time_recorder[k] = None
        self.timer += 1
        start = self.timer
        for adj in self.graph[k]:
            if adj not in self.time_recorder:
                self.dfs(adj)
        end = self.timer
        self.time_recorder[k] = start, end

    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        self.graph = {i: [] for i in xrange(numCourses)}
        for p, q in prerequisites:
            self.graph[p].append(q)
        self.time_recorder = {}
        self.timer = 0
        for i in xrange(numCourses):
            if i not in self.time_recorder:
                self.dfs(i)
        for i in xrange(numCourses):
            t1, t2 = self.time_recorder[i]
            for j in self.graph[i]:
                tt1, tt2 = self.time_recorder[j]
                if not (t1 <= tt1 <= tt2 <= t2 or t1 > tt2):
                    return False
        return True
