# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        def dfs(k, val, reg):
            """ Backtrack curr and res.
                Proceed and evaluate; regret if needed.
                Returns Nothing. """
            if k == n:
                if val == target:
                    res.append(''.join(curr))
                return
            for op in ops:
                curr.append(op)
                for i in xrange(k+1, n+1):
                    proceed(op, k, i, val, reg)
                    if num[k] == '0':
                        break
                curr.pop()

        def proceed(op, k, i, val, reg):
            """ proceed from k to i, ake take [k, i) """
            seg = num[k:i]
            curr.append(seg)
            if op == '+':
                prod = int(seg)
                dfs(i, val+prod, prod)
            elif op == '-':
                prod = -int(seg)
                dfs(i, val+prod, prod)
            elif op == '*':
                prod = reg * int(seg)
                dfs(i, val-reg+prod, prod)
            curr.pop()

        if not num:
            return []

        n = len(num)
        ops = ['+', '-', '*']
        res, curr = [], []
        for i in xrange(1, n+1):
            proceed('+', 0, i, 0, 0)
            if num[0] == '0':
                break
        return res
