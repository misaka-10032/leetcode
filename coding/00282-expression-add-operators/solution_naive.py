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
        def dfs(k):
            if k in partials:
                return partials[k]
            if k == n:
                return ['']
            partial = []
            for op in ops:
                head = op + num[k]
                partial.extend(map(lambda tail: head+tail, dfs(k+1)))
                if num[k] != '0':
                    for i in xrange(k+1, n):
                        head = op + num[k:i+1]
                        partial.extend(map(lambda tail: head+tail, dfs(i+1)))
            partials[k] = partial
            return partial

        def inspect(head, tails):
            for tail in tails:
                exp = head + tail
                if eval(exp) == target:
                    res.append(exp)

        if not num:
            return []
        partials = {}
        ops = ['+', '-', '*']
        n = len(num)
        res = []

        inspect(num[0], dfs(1))
        if num[0] != '0':
            for i in xrange(1, n):
                inspect(num[:i+1], dfs(i+1))
        return res
