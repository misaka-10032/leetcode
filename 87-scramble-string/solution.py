# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        def _check(l1, r1, l2, r2):
            """
            [l1, r1) from s1
            [l2, r2) from s2
            make sure len's are the same outside
            """
            if (l1, r1, l2, r2) in cache:
                return cache[(l1, r1, l2, r2)]
            if r1 == l1 + 1:
                return s1[l1] == s2[l2]
            for k in xrange(1, r1-l1):
                if _check(l1, l1+k, l2, l2+k) and \
                   _check(l1+k, r1, l2+k, r2):
                    # check non-swap
                    cache[(l1, r1, l2, r2)] = True
                    return True
                if _check(l1, l1+k, r2-k, r2) and \
                   _check(l1+k, r1, l2, r2-k):
                    # check swap
                    cache[(l1, r1, l2, r2)] = True
                    return True
            cache[(l1, r1, l2, r2)] = False
            return False

        cache = {}
        if not s1 and not s2:
            return True
        l1 = len(s1)
        l2 = len(s2)
        if l1 != l2:
            return False
        return _check(0, l1, 0, l2)
