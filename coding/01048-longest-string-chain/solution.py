#!/usr/bin/env python3
# encoding: utf-8

from typing import Dict, List, Set


class Solution:
    def _search(self, word: str, word_set: Set[str], cache: Dict[str, int]):
        assert word in word_set
        if word in cache:
            return cache[word]
        if len(word) == 1:
            return 1
        longest = 1
        for i in range(len(word)):
            pred = ''.join([word[:i], word[i + 1:]])
            if pred not in word_set:
                continue
            pred_len = self._search(pred, word_set, cache)
            longest = max(longest, 1 + pred_len)
        cache[word] = longest
        return longest

    def longestStrChain(self, words: List[str]) -> int:
        word_set = set(words)
        cache = {}
        longest = 0
        for word in words:
            new_len = self._search(word, word_set, cache)
            longest = max(longest, new_len)
        return longest
