#!/usr/bin/env python3
# encoding: utf-8

import collections


class Solution:
    def reorganizeString(self, S: str) -> str:
        if not S:
            return ''
        counter = collections.Counter(S)
        sorted_chars = sorted(list(S), key=lambda c: (-counter[c], c))
        n = len(sorted_chars)
        mid = (n + 1) // 2
        if counter[sorted_chars[0]] > mid:
            return ''
        result = [None] * n
        result[::2] = sorted_chars[:mid]
        result[1::2] = sorted_chars[mid:]
        return ''.join(result)
