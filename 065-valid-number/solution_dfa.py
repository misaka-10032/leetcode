# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Start(object):
    def next(self, ch):
        if ch == '+' or ch == '-':
            return Sign()
        elif ch.isdigit():
            return Whole()
        elif ch == '.':
            return Dot()

    def ends(self):
        return False


class Sign(object):
    def next(self, ch):
        if ch.isdigit():
            return Whole()
        elif ch == '.':
            return Dot()

    def ends(self):
        return False


class Whole(object):
    def next(self, ch):
        if ch.isdigit():
            return self
        elif ch == '.':
            return Frac()
        elif ch.lower() == 'e':
            return Exp()

    def ends(self):
        return True


class Dot(object):
    def next(self, ch):
        if ch.isdigit():
            return Frac()

    def ends(self):
        return False


class Frac(object):
    def next(self, ch):
        if ch.isdigit():
            return self
        elif ch.lower() == 'e':
            return Exp()

    def ends(self):
        return True


class Exp(object):
    def next(self, ch):
        if ch == '+' or ch == '-':
            return ExpSign()
        elif ch.isdigit():
            return ExpWhole()

    def ends(self):
        return False


class ExpSign(object):
    def next(self, ch):
        if ch.isdigit():
            return ExpWhole()

    def ends(self):
        return False


class ExpWhole(object):
    def next(self, ch):
        if ch.isdigit():
            return self

    def ends(self):
        return True


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return False
        state = Start()
        for c in s:
            state = state.next(c)
            if not state:
                return False
        return state.ends()
