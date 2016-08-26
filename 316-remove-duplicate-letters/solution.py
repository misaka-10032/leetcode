# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        lasts = {}
        for i, c in enumerate(s):
            lasts[c] = i
        politicians = sorted([(i, c) for c, i in lasts.iteritems()])
        start = 0
        res = []
        for i, c in politicians:
            while c in lasts:
                best = chr(ord(c)+1)
                for j in xrange(start, i+1):
                    if s[j] not in lasts:
                        continue
                    if s[j] < best:
                        best = s[j]
                        start = j+1
                res.append(best)
                lasts.pop(best)
        return ''.join(res)
