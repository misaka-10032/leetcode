# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 0:
            return ''

        if n == 1:
            return '1'

        last = '1'
        for _ in xrange(n-1):
            new = []
            cnt = 1
            for i in xrange(1, len(last)):
                if last[i-1] == last[i]:
                    cnt += 1
                else:
                    new.append(str(cnt))
                    new.append(last[i-1])
                    cnt = 1
            new.append(str(cnt))
            new.append(last[-1])
            last = ''.join(new)

        return last
