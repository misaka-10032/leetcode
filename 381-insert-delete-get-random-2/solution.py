# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from random import randint


class RandomizedCollection(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.v2i = {}

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.v2i:
            self.v2i[val].add(len(self.vals))
            self.vals.append(val)
            return False
        else:
            self.v2i[val] = {len(self.vals)}
            self.vals.append(val)
            return True

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.v2i:
            return False
        val_indices = self.v2i[val]
        i = val_indices.pop()     # rm v2i
        if i != len(self.vals)-1:
            last = self.vals[-1]
            last_indices = self.v2i[last]
            last_indices ^= {len(self.vals)-1, i}  # switch index for last
            self.vals[i] = last                    # switch vals
        self.vals.pop()           # rm val
        if not val_indices:
            self.v2i.pop(val)
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        i = randint(0, len(self.vals)-1)
        return self.vals[i]


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
