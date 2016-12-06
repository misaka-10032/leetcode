# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

import re


class Solution(object):
    p = re.compile('^\ *[+-]?(\d*\.?\d+|\d+\.?\d*)(e[+-]?\d+)?\ *$')

    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        return bool(self.p.match(s))
