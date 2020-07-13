#!/usr/bin/env python3
# encoding: utf-8


class Solution:
    def find_mismatch(self, s: str, start: int, end: int):
        # Finds the first mismatch index. Returns -1 if the str
        # is palindrome. Start is inclusive. End is exclusive.
        idx = start
        mid = (start + end - 1) // 2
        while idx <= mid:
            if s[idx] != s[start + end - 1 - idx]:
                return idx
            idx += 1
        return -1

    def validPalindrome(self, s: str) -> bool:
        mismatch = self.find_mismatch(s, 0, len(s))
        if mismatch < 0:
            return True
        # Try deleting the left element
        mismatch1 = self.find_mismatch(s, mismatch + 1, len(s) - mismatch)
        if mismatch1 < 0:
            return True
        # Try deleting the right element
        mismatch2 = self.find_mismatch(s, mismatch, len(s) - mismatch - 1)
        if mismatch2 < 0:
            return True
        return False
