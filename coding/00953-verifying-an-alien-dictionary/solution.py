#!/usr/bin/env python3
# encoding: utf-8

from typing import Dict, List


class Solution:
    def convert_to_regular(self, word: str, alien_to_regular_map: Dict[str, str]):
        chars = []
        for c in word:
            chars.append(alien_to_regular_map[c])
        return ''.join(chars)

    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alien_to_regular_map = {}
        for idx in range(len(order)):
            alien_to_regular_map[order[idx]] = chr(idx + ord('a'))
        for idx in range(len(words) - 1):
            regular_word1 = self.convert_to_regular(words[idx], alien_to_regular_map)
            regular_word2 = self.convert_to_regular(words[idx + 1], alien_to_regular_map)
            if regular_word1 > regular_word2:
                return False
        return True
