# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class State(object):
    def __init__(self):
        self.trans = {}
        self.any = False

    def next(self, c, states=None):
        """
        :param c:
        :param states: update new states into it.
        :return: set of next possible states.
        """
        r = set() if states is None else states
        if c is None:
            _states = self.trans.get(None)
            if _states:
                for state in _states:
                    r.add(state)
                    state.next(None, r)
        else:
            _states = self.trans.get(c)
            if _states:
                r.update(_states)
            _states = self.trans.get('.')
            if _states:
                r.update(_states)
            _states = self.trans.get(None)
            if _states:
                for state in _states:
                    state.next(c, r)
        return r

    def add_trans(self, c, state):
        if c in self.trans:
            self.trans[c].add(state)
        else:
            self.trans[c] = {state}


class Solution(object):
    def _accept(self, curr, end):
        if curr is None:
            return False
        states = curr.next(None, {curr})
        for state in states:
            if state is end:
                return True
        return False

    def _build_state_machine(self, pattern):
        _len = len(pattern)
        start = prevstate = currstate = State()
        prevchar = currchar = None
        i = 0
        while i < _len:
            """ currchar is guaranteed != '*' """
            currchar = pattern[i]
            if i+1 >= _len or pattern[i+1] != '*':
                currstate = State()
            else:
                if prevchar != currchar:
                    currstate = State()
                    prevstate.add_trans(None, currstate)
                    prevstate = currstate
                i += 1
            prevchar = currchar
            prevstate.add_trans(currchar, currstate)
            prevstate = currstate
            i += 1
        end = currstate
        return start, end

    def _search_state(self, s, i, curr, end):
        """
        Before taking in ith char in s, we are in state state,
        return if such condition is accepted.
        :param s:
        :param i:
        :param curr:
        :param end:
        :return:
        """
        if i >= len(s):
            return self._accept(curr, end)
        states = curr.next(s[i])
        for state in states:
            ac = self._search_state(s, i+1, state, end)
            if ac:
                return True
        return False

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not s and not p:
            return True
        if s and not p:
            return False
        start, end = self._build_state_machine(p)
        return self._search_state(s, 0, start, end)
