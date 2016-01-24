# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

BFS.
"""
__author__ = 'misaka-10032'

from collections import deque


class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        letters = {
            '0': ' ',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        digits = digits.replace('1', '')
        len_digits = len(digits)
        states = deque()
        states.append('')
        sol = []
        while states:
            st = states.popleft()
            p = len(st)
            if p >= len_digits:
                if st:
                    sol.append(st)
                continue
            for c in letters[digits[p]]:
                states.append(st+c)
        return sol
