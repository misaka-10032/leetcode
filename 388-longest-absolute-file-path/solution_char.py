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
        # trick to handle last file
        input += '\n'
        # stores the size of subdirs up to here
        stack = deque([0])
        # current size of dir/file
        curr = 0
        is_file = False
        longest = 0
        i = 0
        while i < len(input):
            c = input[i]
            if c == '\n':
                if is_file:
                    longest = max(longest, stack[-1]+curr)
                    curr = 0
                    i += 1
                    is_file = False
                else:
                    # dir and separator
                    stack.append(stack[-1]+curr+1)
                    curr = 0
                    i += 1
                # determine next level
                level = 0
                while i < len(input) and input[i] == '\t':
                    level += 1
                    i += 1
                to_pop = len(stack) - level - 1
                for _ in xrange(to_pop):
                    stack.pop()
            elif c == '.':
                is_file = True
                curr += 1
                i += 1
            else:
                # just normal characters
                i += 1
                curr += 1
        return longest
