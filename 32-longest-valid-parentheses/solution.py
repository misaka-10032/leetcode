# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:  # ')'
                if stack and s[stack[-1]] == '(':
                    # match up
                    stack.pop()
                else:
                    # push ')' as indicator of mismatch
                    stack.append(i)

        if not stack:
            # perfect
            return len(s)

        i = 0
        max_cnt = 0
        # tricky end-indicator
        stack.append(len(s))
        for j in stack:
            cnt = j - i
            if cnt > max_cnt:
                max_cnt = cnt
            i = j + 1

        return max_cnt
