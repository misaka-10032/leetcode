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

    def _solve(self, sol_lst, sol, candidates, freq, rb, target):
        if target == 0:
            # need to copy sol
            sol_lst.append(sorted(sol))
            return
        i_last = self._find(candidates, target, 0, rb)
        for i in xrange(i_last, -1, -1):
            for f in xrange(freq[i], 0, -1):
                c = candidates[i]
                if c * f > target:
                    continue
                sol.extend([c]*f)
                self._solve(sol_lst, sol, candidates, freq, i-1, target-c*f)
                del sol[-f:]

    def combinationSum2(self, candidates, target):
        """
        The only difference lies in duplicate in candidates
        As result shouldn't contain duplicate, we can turn the candidates into
        a list of unique elements and their frequencies.

        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not candidates:
            return []

        candidates = sorted(candidates)
        c, f = [candidates[0]], [1]
        for i in xrange(1, len(candidates)):
            if candidates[i-1] == candidates[i]:
                f[-1] += 1
            else:
                c.append(candidates[i])
                f.append(1)

        sol_lst, sol = [], []
        self._solve(sol_lst, sol, c, f, len(c)-1, target)
        return sorted(sol_lst)
