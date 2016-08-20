# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from random import randint


class RandomizedSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.v2i = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.v2i:
            return False
        self.v2i[val] = len(self.vals)
        self.vals.append(val)
        return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.v2i:
            return False
        i = self.v2i[val]
        self.v2i[self.vals[-1]] = i
        self.vals[i], self.vals[-1] = self.vals[-1], self.vals[i]
        self.vals.pop()
        self.v2i.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        i = randint(0, len(self.vals)-1)
        return self.vals[i]
