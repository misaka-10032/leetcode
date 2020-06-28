# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        f = [0] * (n+1)
        """ [0, 1) and [1, 1) are palindromes
            0 don't need to be put in the list """
        prev = [1]
        for i in xrange(2, n+1):
            best = 1 + f[i-1]
            """ [i-1, i) and [i, i) are palindromes """
            curr = [i-1, i]
            for j in prev:
                """ [j, i-1)'s are palindromes """
                if j > 0 and s[j-1] == s[i-1]:
                    if j == 1:
                        best = 0
                    else:
                        curr.append(j-1)
                        best = min(best, 1+f[j-1])
            f[i] = best
            prev = curr
        return f[n]
