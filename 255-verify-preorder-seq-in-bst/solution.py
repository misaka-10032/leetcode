# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        if not preorder:
            return True

        # strict lower bound
        lb = -999999999
        # elements in the stack will be non-increasing
        stack = deque([preorder[0]])
        for curr in preorder[1:]:
            while stack and curr >= stack[-1]:
                lb = stack.pop()
            if curr <= lb:
                return False
            stack.append(curr)
        return True
