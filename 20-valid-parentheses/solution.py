# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def isValid(self, s):
        """
        stack up chars. Ensure that finally stack is empty.
        edge case: empty list.

        :type s: str
        :rtype: bool
        """
        match = {
            '(': ')',
            '{': '}',
            '[': ']',
        }
        stack = []
        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if match[top] != c:
                    return False
        if not stack:
            return True
        else:
            return False
