# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: Set[str]
        :rtype: bool
        """
        if not s:
            return True
        if not wordDict:
            return False

        n = len(s)
        f = [False] * (n+1)
        f[0] = True
        for i in xrange(1, n+1):
            for word in wordDict:
                if not s.endswith(word, 0, i):
                    continue
                f[i] |= f[i-len(word)]
                if f[i]:
                    break
        return f[n]
