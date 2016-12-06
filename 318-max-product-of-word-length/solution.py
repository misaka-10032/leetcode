# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        def hash(w):
            v = 0
            for c in w:
                v |= 1 << (ord(c) - ord('a'))
            return v

        hashes = [0] * len(words)
        for i, w in enumerate(words):
            hashes[i] = hash(w)

        best = 0
        for i, w1 in enumerate(words):
            for j, w2 in enumerate(words):
                if hashes[i] & hashes[j] == 0:
                    best = max(best, len(w1)*len(w2))
        return best
