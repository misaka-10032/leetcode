# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def hash_to_str(v):
            r = []
            for i in xrange(10):
                r.append(v2c[v % 4])
                v >>= 2
            return ''.join(reversed(r))

        if len(s) <= 10:
            return []

        curr = 0
        c2v = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
        v2c = ['A', 'C', 'G', 'T']
        for i in xrange(10):
            curr <<= 2
            curr += c2v[s[i]]
        appeared = {curr}
        dup = set()
        for i in xrange(10, len(s)):
            curr -= c2v[s[i-10]] << 18
            curr <<= 2
            curr += c2v[s[i]]
            if curr in appeared:
                dup.add(hash_to_str(curr))
            else:
                appeared.add(curr)
        return list(dup)
