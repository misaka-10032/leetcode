# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""

from collections import deque


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: Set[str]
        :rtype: int
        """
        def next_word(word):
            for i in xrange(len(word)):
                before = word[:i]
                after = word[i+1:]
                for ci in xrange(26):
                    c = chr(ci+ord('a'))
                    new = before + c + after
                    if new in wordList or new == endWord:
                        yield new

        if beginWord == endWord:
            return 1
        curr_level = deque([beginWord])
        dist = 1
        appeared = {beginWord}
        while curr_level:
            dist += 1
            next_level = deque()
            for word in curr_level:
                for word_next in next_word(word):
                    if word_next == endWord:
                        return dist
                    if word_next not in appeared:
                        next_level.append(word_next)
                        appeared.add(word_next)
            curr_level = next_level
        return 0
