#!/usr/bin/env python3
# encoding: utf-8


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        keep_arr = [True for _ in range(len(s))]
        left_cnt = 0
        for idx, c in enumerate(s):
            if c == '(':
                left_cnt += 1
            elif c == ')':
                if left_cnt > 0:
                    left_cnt -= 1
                else:
                    keep_arr[idx] = False
        right_cnt = 0
        for r_idx, c in enumerate(reversed(s)):
            idx = len(s) - 1 - r_idx
            if c == ')':
                right_cnt += 1
            elif c == '(':
                if right_cnt > 0:
                    right_cnt -= 1
                else:
                    keep_arr[idx] = False
        kept_chars = []
        for keep, c in zip(keep_arr, s):
            if keep:
                kept_chars.append(c)
        return ''.join(kept_chars)
