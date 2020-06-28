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
        def _dfs(k):
            if k == n:
                all.append(' '.join(curr))
                return
            for word in wordDict:
                if s.startswith(word, k):
                    curr.append(word)
                    _dfs(k+len(word))
                    curr.pop()

        n = len(s)
        maxlen = 0
        for word in wordDict:
            maxlen = max(maxlen, len(word))
        wordDict = set(wordDict)
        all = []
        curr = []
        _dfs(0)
        return all
