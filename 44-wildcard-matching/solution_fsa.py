# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class State(object):
    def __init__(self):
        self.trans = {}
        self.is_end = False


class Solution(object):
    def _build_state_machine(self, pattern):
        start = State()
        p = start
        for c in pattern:
            if c == '*':
                p.trans[c] = p
            else:
                q = State()
                p.trans[c] = q
                p = q
        p.is_end = True
        return start

    def _dfs(self, state, s, k):
        if k == len(s):
            return state.is_end
        if s[k] in state.trans:
            if self._dfs(state.trans[s[k]], s, k+1):
                return True
        if '?' in state.trans:
            if self._dfs(state.trans['?'], s, k+1):
                return True
        if '*' in state.trans:
            if self._dfs(state.trans['*'], s, k+1):
                return True
        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            if not s:
                return True
            else:
                return False

        start = self._build_state_machine(p)
        return self._dfs(start, s, 0)
