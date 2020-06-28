# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* sort all chars
* defaultdict: char -> set of neighbors
* build graph
  * find the critical dependency
* edge case
  * 'ab' will by no means appear before 'a'
"""

from collections import defaultdict


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        def dfs(u):
            for v in adj[u]:
                if visited[v]:
                    continue

                timer[0] += 1
                t_in = timer[0]
                visited[v] = True

                dfs(v)

                timer[0] += 1
                t_out = timer[0]
                res.append(v)
                times[v] = t_in, t_out

        adj = defaultdict(set)
        vertices = set()
        prev = None
        for word in words:
            if not word:
                continue
            for c in word:
                vertices.add(c)
            if not prev:
                prev = word
                continue

            i = j = 0
            while i < len(prev) and j < len(word):
                if prev[i] != word[j]:
                    break
                i += 1
                j += 1

            if i < len(prev) and j == len(word):
                return ''
            elif i < len(prev) and j < len(word):
                adj[prev[i]].add(word[j])

            prev = word

        visited = {k: False for k in vertices}
        times = {}  # in/out time
        timer = [0]
        res = []

        # topsort
        for v in vertices:
            if visited[v]:
                continue

            timer[0] += 1
            t_in = timer[0]
            visited[v] = True

            dfs(v)

            timer[0] += 1
            t_out = timer[0]
            res.append(v)
            times[v] = t_in, t_out

        for u in vertices:
            prev = times[u]
            for v in adj[u]:
                curr = times[v]
                if prev[0] < curr[0] < curr[1] < prev[1] or \
                   prev[0] > curr[1]:
                    continue
                else:
                    return ''
        return ''.join(reversed(res))
