# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

DFS. A bit faster than BFS, because str (immutable) operation is time consuming.
"""
__author__ = 'misaka-10032'


class Solution(object):
    letters = [
        ' ',        # 0
        '',         # 1
        'abc',      # 2
        'def',      # 3
        'ghi',      # 4
        'jkl',      # 5
        'mno',      # 6
        'pqrs',     # 7
        'tuv',      # 8
        'wxyz',     # 9
    ]

    def dfs(self, digits, curr, sol):
        """
        :param curr: list[char]
        :param sol:
        :return:
        """
        p = len(curr)
        if p >= len(digits):
            comb = ''.join(curr)
            if comb:
                sol.append(comb)
            return
        idx = ord(digits[p]) - ord('0')
        for c in self.letters[idx]:
            curr.append(c)
            self.dfs(digits, curr, sol)
            curr.pop()

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        digits = digits.replace('1', '')
        sol = []
        self.dfs(digits, [], sol)
        return sol
