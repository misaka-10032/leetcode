# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

"""


class Solution(object):
    def is_parlindrome(self, word, start, end):
        """ check if s[start:end) is parlindrome """
        p, q = start, end-1
        while p < q:
            if word[p] != word[q]:
                return False
            p += 1
            q -= 1
        return True

    def dict_append(self, d, word, idx):
        if word in d:
            d[word].append(idx)
        else:
            d[word] = [idx]

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # key: word
        # val: list of 1st indices
        leftc = {}   # left complement
        rightc = {}  # right complement
        for i, word in enumerate(words):
            wl = len(word)
            if self.is_parlindrome(word, 0, wl):
                self.dict_append(leftc, "", i)
                self.dict_append(rightc, "", i)
            self.dict_append(leftc, word[::-1], i)
            self.dict_append(rightc, word[::-1], i)
            for j in xrange(1, wl+1):
                if self.is_parlindrome(word, j, wl):
                    self.dict_append(rightc, word[j-1::-1], i)
                if self.is_parlindrome(word, 0, j):
                    self.dict_append(leftc, word[:j-1:-1], i)
        match = set()
        for i, word in enumerate(words):
            if word in leftc:
                for j in leftc[word]:
                    if i != j:
                        match.add((i, j))
            if word in rightc:
                for j in rightc[word]:
                    if i != j:
                        match.add((j, i))
        return map(list, list(match))
