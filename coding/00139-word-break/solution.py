# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* f[i] denotes if s[:i] is compound word
* Easier expression but a little bit counter intuitive
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
        f = [False] * (m+1)
        f[0] = True  # empty word is step under all others
        # k is len of prefix
        for k in xrange(1, m+1):
            # l is suffix len of prefix
            for l in xrange(min_len, max_len+1):
                if k-l < 0:
                    break
                f[k] = f[k-l] and s[k-l:k] in wordDict
                if f[k]:
                    break
        return f[-1]
