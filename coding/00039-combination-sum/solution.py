# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def _find(self, candidates, target, lb, rb):
        """ Find the first index whose value <= target.
            Could be -1 if all > target """
        # we'v made sure there's no duplicate in candidates
        li, ri = lb, rb
        while li < ri:
            mi = (li + ri) // 2
            if candidates[mi] < target:
                li = mi + 1
            elif candidates[mi] > target:
                ri = mi - 1
            else:
                return mi

        if li == ri:
            if candidates[li] <= target:
                return li
            else:
                return li - 1

        if ri < lb:
            return ri

        if li == rb:
            return rb - 1

        # now it's like c[ri] < target < c[li]
        # actually these 3 cases are all ri...
        return ri

    def _solve(self, sol_lst, sol, candidates, rb, target):
        if target == 0:
            # need to copy sol
            sol_lst.append(sorted(sol))
            return
        i_last = self._find(candidates, target, 0, rb)
        for i in xrange(i_last, -1, -1):
            c = candidates[i]
            sol.append(c)
            self._solve(sol_lst, sol, candidates, i, target-c)
            sol.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates = sorted(set(candidates))
        sol_lst, sol = [], []
        self._solve(sol_lst, sol, candidates, len(candidates)-1, target)
        return sorted(sol_lst)
