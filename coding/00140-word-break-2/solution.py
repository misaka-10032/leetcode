#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        cache = [None for _ in range(len(s))]
        # Searches all the possible sentences starting at i (aka s[i:]).
        def _search(i: int) -> List[str]:
            if cache[i] is not None:
                return cache[i]
            sentences = []
            for word in wordDict:
                if s.startswith(word, i):
                    if i+len(word) == len(s):
                        sentences.append(word)
                    else:
                        sentences_after_word = _search(i+len(word))
                        for sentence in sentences_after_word:
                            sentences.append(' '.join([word, sentence]))
            cache[i] = sentences
            return sentences
        if not s:
            return []
        return _search(0)
