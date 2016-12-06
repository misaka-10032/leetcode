# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string.

        :type strs: List[str]
        :rtype: str
        """
        r = [str(len(strs))]
        for s in strs:
            r.append(str(len(s)))
            r.append(s)
        return ' '.join(r)

    def decode(self, s):
        """Decodes a single string to a list of strings.

        :type s: str
        :rtype: List[str]
        """
        q = 0
        p = s.find(' ')
        p = p if p > 0 else len(s)
        listlen = int(s[q:p])

        strs = []
        for _ in xrange(listlen):
            q = p + 1
            p = s.find(' ', q)
            strlen = int(s[q:p])
            q = p + 1
            p = q + strlen
            strs.append(s[q:p])
        return strs
