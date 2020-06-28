# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class ValidWordAbbr(object):
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.d = {}
        for w in dictionary:
            if len(w) <= 2:
                continue
            abbr = w[0] + str(len(w)-2) + w[-1]
            if abbr in self.d:
                self.d[abbr].add(w)
            else:
                self.d[abbr] = {w}

    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        if len(word) <= 2:
            abbr = word
        else:
            abbr = word[0] + str(len(word)-2) + word[-1]
        if abbr not in self.d:
            return True
        else:
            wset = self.d[abbr]
            if word in wset:
                return len(wset) == 1
            else:
                return False
