# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

# TODO: my understanding of reference solution
* 00 is must-lose
* 01 is must-win
* 10 is being able to choose lose; may try to win, but may still lose.
* 11 is being able to choose win; may try to lose, but may still win.
"""

import re


class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # TODO

        # g, G = [0], 0
        # for p in map(len, re.split('-+', s)):
        #     while len(g) <= p:
        #         g += min(set(range(p)) - {a ^ b for a, b in zip(g, g[-2::-1])}),
        #     G ^= g[p]
        #
        # dbg = map('{:02b}'.format, g)
        # print dbg
        #
        # return G > 0

        # subs = re.split('-+', s)
        # subs = map(len, subs)
        # l_max = max(subs)
        # f = [0] * max(3, l_max+1)
        # f[0] = f[1] = 0
        # f[2] = 1
        # for k in xrange(3, l_max+1):
        #     for l1 in xrange(0, k-1):
        #         f[k] |= f[l1] == f[k-l1-2]
        # win = False
        # for sub in subs:
        #     win ^= f[sub]
        # return win
