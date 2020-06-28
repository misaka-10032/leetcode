# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def infix_to_postfix(s):
            S = deque()
            t = []
            n = len(s)
            i = 0
            while i < n:
                c = s[i]
                if c.isdigit():
                    j = i
                    while j < n and s[j].isdigit():
                        j += 1
                    t.append(s[i:j])
                    i = j
                elif c == '(':
                    S.append(c)
                    i += 1
                elif c == ')':
                    while S[-1] != '(':
                        t.append(S.pop())
                    S.pop()
                    i += 1
                else:  # operators
                    while S and S[-1] != '(' and w[S[-1]] >= w[c]:
                        t.append(S.pop())
                    S.append(c)
                    i += 1
            while S:
                t.append(S.pop())
            return t

        def eval_postfix(t):
            S = deque()
            for item in t:
                if item[0].isdigit():
                    S.append(item)
                else:
                    op2 = int(S.pop())
                    op1 = int(S.pop())
                    if item == '+':
                        S.append(op1+op2)
                    elif item == '-':
                        S.append(op1-op2)
                    else:  # *
                        S.append(op1*op2)
            return int(S[-1])

        s = s.replace(' ', '')
        if not s:
            return 0
        w = {'+': 1, '-': 1, '*': 2}
        return eval_postfix(infix_to_postfix(s))
