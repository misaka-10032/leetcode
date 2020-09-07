#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        doomed = [False for _ in range(len(s))]
        # Returns whether s[i:] can be broken successfully.
        def _search(i: int) -> bool:
            if i == len(s):
                return True
            if doomed[i]:
                return False
            for word in wordDict:
                if s.startswith(word, i):
                    success = _search(i+len(word))
                    if success:
                        return True
            doomed[i] = True
            return False
        return _search(0)
