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
            """ returns list(list(str)) as all possible sentences
                using s[k:]. """
            if k in cache:
                return cache[k]
            res = []
            for word in wordDict:
                if s.startswith(word, k):
                    if k + len(word) == n:
                        res.append([word])
                    else:
                        after = _dfs(k+len(word))
                        for sent in after:
                            res.append([word] + sent)
            cache[k] = res
            return res

        if not s or not wordDict:
            return []

        n = len(s)
        cache = {}
        return map(lambda sent: ' '.join(sent), _dfs(0))
