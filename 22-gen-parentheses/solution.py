# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Solution(object):
    def _gen(self, ps, curr_str, pos, n, n_left, n_right):
        """
        :param ps: Global list to save all the parentheses
        :param curr_str: The current char list.
            Don't use string for performance consideration.
        :param pos: The current position
        :param n: # parentheses to generate
        :param n_left: # left parentheses generated
        :param n_right: # right parentheses generated
        :return:
        """
        if pos == 2*n:
            ps.append(''.join(curr_str))
        else:
            if n_left < n:
                curr_str[pos] = '('
                self._gen(ps, curr_str, pos+1, n, n_left+1, n_right)
            if n_left > n_right:
                curr_str[pos] = ')'
                self._gen(ps, curr_str, pos+1, n, n_left, n_right+1)
        return ps

    def generateParenthesis(self, n):
        """
        DFS
        :type n: int
        :rtype: List[str]
        """
        if n == 0:
            return []
        ps = []
        curr_str = [None] * (n*2)
        return self._gen(ps, curr_str, 0, n, 0, 0)
