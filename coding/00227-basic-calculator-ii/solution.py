#!/usr/bin/env python3
# encoding: utf-8

from typing import Tuple, Union


class Solution:
    def parse_next(self, s: str, start: int) -> Tuple[Union[None, str, int], int]:
        idx = start
        while idx < len(s) and s[idx] == ' ':
            idx += 1
        if idx == len(s):
            return None, idx
        if s[idx].isdigit():
            num = 0
            while idx < len(s) and s[idx].isdigit():
                num = num * 10 + ord(s[idx]) - ord('0')
                idx += 1
            return num, idx
        else:
            return s[idx], idx + 1

    def update_prod(self, curr_prod: int, curr_prod_op: str, curr_item: int):
        if curr_prod_op == '*':
            return curr_prod * curr_item
        elif curr_prod_op == '/':
            return curr_prod // curr_item
        else:
            assert 0

    def update_sum(self, curr_sum: int, curr_sum_op: str, curr_prod: int):
        if curr_sum_op == '+':
            return curr_sum + curr_prod
        elif curr_sum_op == '-':
            return curr_sum - curr_prod
        else:
            assert 0

    def eval(self, s: str, start: int):
        idx = start
        prev_is_num = False
        curr_sum = 0
        curr_prod = 1
        curr_sum_op = '+'
        curr_prod_op = '*'
        while idx < len(s):
            curr_item, next_idx = self.parse_next(s, idx)
            if isinstance(curr_item, int):
                curr_prod = self.update_prod(curr_prod, curr_prod_op, curr_item)
                prev_is_num = True
            elif curr_item == '-' and not prev_is_num:
                curr_sum_op = '-' if curr_sum_op == '+' else '+'
            elif curr_item in ('+', '-'):
                curr_sum = self.update_sum(curr_sum, curr_sum_op, curr_prod)
                curr_sum_op = curr_item
                curr_prod_op = '*'
                curr_prod = 1
                prev_is_num = False
            elif curr_item in ('*', '/'):
                curr_prod_op = curr_item
                prev_is_num = False
            else:
                assert next_idx == len(s)
                break
            idx = next_idx
        if prev_is_num:
            return self.update_sum(curr_sum, curr_sum_op, curr_prod)
        else:
            return 0

    def calculate(self, s: str) -> int:
        return self.eval(s, 0)
