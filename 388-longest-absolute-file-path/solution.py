# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        longest = 0
        stack = deque([0])
        for line in input.splitlines():
            name = line.lstrip('\t')
            to_pop = len(stack) - (len(line)-len(name)+1)
            for _ in xrange(to_pop):
                stack.pop()
            if '.' in name:
                longest = max(longest, stack[-1]+len(name))
            else:
                stack.append(stack[-1]+1+len(name))
        return longest
