# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def justify_mid(line, sz):
            if len(line) == 1:
                return line[0] + ' '*(maxWidth-sz)
            r = maxWidth - sz
            avg = r // (len(line)-1)
            # how many spaces need one more
            more = r - avg * (len(line)-1)
            # append those need more
            t = []
            t.append(line[0])
            for i in xrange(more):
                t.append(' '*(2+avg))
                t.append(line[i+1])
            for i in xrange(more, len(line)-1):
                t.append(' '*(1+avg))
                t.append(line[i+1])
            return ''.join(t)

        def justify_last(line, sz):
            return ' '.join(line) + ' '*(maxWidth-sz)

        words = words[::-1]
        res = []
        sz = 0
        line = []
        while words:
            if not line or sz+1+len(words[-1]) <= maxWidth:
                w = words.pop()
                sz += len(w)
                sz += 1 if line else 0
                line.append(w)
            else:
                if words:
                    res.append(justify_mid(line, sz))
                else:
                    res.append(justify_last(line, sz))
                line = []
                sz = 0
        if line:
            res.append(justify_last(line, sz))
        return res
