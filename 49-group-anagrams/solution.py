# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def groupAnagrams(self, strs):
        """
        Use sorted str as key. Convert that to tuple of chars in order to be key.

        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for s in strs:
            key = tuple(sorted(s))
            if key in d:
                d[key].append(s)
            else:
                d[key] = [s]
        return d.values()
