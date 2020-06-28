# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Below is the interface for Iterator, which is already defined for you.
class Iterator(object):
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """
        self.i = 0
        self.nums = nums

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.i != len(self.nums)

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        x = self.nums[self.i]
        self.i += 1
        return x


class PeekingIterator(object):
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.cache = None
        self.ahead = iterator.next() if iterator.hasNext() else None
        self.it = iterator

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.ahead

    def next(self):
        """
        :rtype: int
        """
        self.cache = self.ahead
        self.ahead = self.it.next() if self.it.hasNext() else None
        return self.cache

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.ahead is not None


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].
