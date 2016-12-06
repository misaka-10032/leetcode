# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


from collections import deque


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        stack = deque([[[], 1]])
        cnt_lst = []
        for c in s:
            if c.isdigit():
                cnt_lst.append(c)
            elif c == '[':
                stack.append([[], int(''.join(cnt_lst))])
                cnt_lst = []
            elif c == ']':
                c_lst, cnt = stack.pop()
                stack[-1][0].extend(c_lst * cnt)
            else:
                stack[-1][0].append(c)
        return ''.join(stack[0][0])
