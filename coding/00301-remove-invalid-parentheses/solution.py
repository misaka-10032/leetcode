#!/usr/bin/env python3
# encoding: utf-8


from typing import List, Set, Tuple


class Solution:
    # s, init_idx, init_idx, left_rm_cnt, right_rm_cnt, kept_chars, sol
    def remove_recur(
            self, s: str, curr_idx: int, curr_left_cnt: int,
            left_rm_budget: int, right_rm_budget: int, kept_chars: List[str], sol: Set[str]):
        if curr_idx == len(s):
            if curr_left_cnt == 0:
                sol.add(''.join(kept_chars))
            return
        curr_char = s[curr_idx]
        if curr_char == '(':
            # Choice 1: keep it.
            kept_chars.append(curr_char)
            self.remove_recur(
                s, curr_idx + 1, curr_left_cnt + 1, left_rm_budget, right_rm_budget, kept_chars, sol)
            kept_chars.pop()
            if left_rm_budget > 0:
                # Choice 2: remove it.
                self.remove_recur(
                    s, curr_idx + 1, curr_left_cnt, left_rm_budget - 1, right_rm_budget, kept_chars, sol)
        elif curr_char == ')':
            if curr_left_cnt > 0:
                # Choice 1: keep it.
                kept_chars.append(curr_char)
                self.remove_recur(
                    s, curr_idx + 1, curr_left_cnt - 1, left_rm_budget, right_rm_budget, kept_chars, sol)
                kept_chars.pop()
            if right_rm_budget > 0:
                # Choice 2: remove it.
                self.remove_recur(
                    s, curr_idx + 1, curr_left_cnt, left_rm_budget, right_rm_budget - 1, kept_chars, sol)
        else:
            # Always keep other chars.
            kept_chars.append(curr_char)
            self.remove_recur(
                s, curr_idx + 1, curr_left_cnt, left_rm_budget, right_rm_budget, kept_chars, sol)
            kept_chars.pop()

    def remove_greedy(self, s: str) -> Tuple[str, int, int]:
        keep_arr = [True for _ in range(len(s))]
        left_cnt = 0
        right_rm_cnt = 0
        for idx, c in enumerate(s):
            if c == '(':
                left_cnt += 1
            elif c == ')':
                if left_cnt == 0:
                    right_rm_cnt += 1
                    keep_arr[idx] = False
                else:
                    left_cnt -= 1
        right_cnt = 0
        left_rm_cnt = 0
        for r_idx, c in enumerate(reversed(s)):
            idx = len(s) - 1 - r_idx
            if c == ')':
                right_cnt += 1
            elif c == '(':
                if right_cnt == 0:
                    left_rm_cnt += 1
                    keep_arr[idx] = False
                else:
                    right_cnt -= 1
        kept_chars = []
        for idx, keep in enumerate(keep_arr):
            if keep:
                kept_chars.append(s[idx])
        return ''.join(kept_chars), left_rm_cnt, right_rm_cnt

    def removeInvalidParentheses(self, s: str) -> List[str]:
        greedy_sol, left_rm_cnt, right_rm_cnt = self.remove_greedy(s)
        if not greedy_sol:
            return [""]
        sol = set([greedy_sol])
        init_idx = left_cnt = 0
        kept_chars = []
        self.remove_recur(
            s, init_idx, left_cnt, left_rm_cnt, right_rm_cnt, kept_chars, sol)
        return list(sol)
