# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* f[i] denotes if s[:i+1] is compound word
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

        wordDict = set(wordDict)
        min_len = 999999999
        max_len = -1
        for word in wordDict:
            min_len = min(min_len, len(word))
            max_len = max(max_len, len(word))

        m = len(s)
        f = [False] * m
        for i in xrange(m):
            for l in xrange(min_len, max_len+1):
                if i-l+1 < 0:
                    break
                prev = f[i-l] if i-l >= 0 else True
                f[i] = prev and s[i-l+1:i+1] in wordDict
                if f[i]:
                    break
        return f[-1]
