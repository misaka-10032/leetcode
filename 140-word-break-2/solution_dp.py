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
        :rtype: List[str]
        """
        if not s or not wordDict:
            return []

        n = len(s)
        wordDict = set(wordDict)
        l_min = 999999999
        l_max = -1
        for word in wordDict:
            m = len(word)
            l_min = min(l_min, m)
            l_max = max(l_max, m)

        # list of list of list
        f = [[] for _ in xrange(n)]
        for k in xrange(n-1, -1, -1):
            if s[k:] in wordDict:
                # list of list rather than list of str
                # because str concat is costly
                f[k] = [[s[k:]]]
            for l in xrange(l_min, l_max+1):
                if k+l >= n:
                    break
                start = s[k:k+l]
                if start in wordDict:
                    for suffix in f[k+l]:
                        print k, k+l, len(suffix), suffix
                        f[k].append([start] + suffix)

        return map(lambda clst: ' '.join(clst), f[0])
