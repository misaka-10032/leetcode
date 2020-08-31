#!/usr/bin/env python3
# encoding: utf-8


class Solution:
    def isValidPalindrome(self, s: str, k: int) -> bool:
        # f[left][right] defines the minimal budget required to make
        # a valid palindrome within s[left:right+1].
        n = len(s)
        f = [[None for _ in range(n)] for _ in range(n)]
        for left in range(n):
            f[left][left] = 0
        for length in range(2, n+1):
            for left in range(n-length+1):
                right = left + length - 1
                budget1 = k + 1
                if s[left] == s[right]:
                    budget1 = 0
                    if left+1 <= right-1:
                        budget1 += f[left+1][right-1]
                budget2 = 1 + f[left+1][right]
                budget3 = 1 + f[left][right-1]
                min_budget = min(budget1, budget2, budget3)
                f[left][right] = min_budget
        return f[0][n-1] <= k
