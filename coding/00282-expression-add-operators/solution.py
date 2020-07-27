#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:

    def _make_expr(self, num: str, ops: List[str]) -> str:
        expr = []
        assert len(num) == len(ops) + 1
        for num_char, op in zip(num, ops):
            expr.append(num_char)
            expr.append(op)
        expr.append(num[-1])
        return ''.join(expr)

    def _search(self, num: str, target: int, idx: int,
                curr_num: int, curr_prod: int, curr_sum: int,
                ops: List[str], results: List[str]):
        curr_num = curr_num * 10 + int(num[idx])
        # num_idx tracks the last *start* index of the number.
        if idx == len(num) - 1:
            final_sum = curr_sum + curr_prod * curr_num
            if final_sum == target:
                expr = self._make_expr(num, ops)
                results.append(expr)
            return
        # Case 1: continue the number. Leading 0's are not allowed.
        if curr_num != 0:
            ops.append('')
            self._search(num, target, idx + 1, curr_num, curr_prod, curr_sum, ops, results)
            ops.pop()
        # Case 2: +. Reset curr_num to 0. Reset curr_prod to 1. Aggregate curr_sum.
        ops.append('+')
        self._search(num, target, idx + 1, 0, 1, curr_sum + curr_prod * curr_num, ops, results)
        ops.pop()
        # Case 3: -. Reset curr_num to 0. Reset curr_prod to -1. Aggregate curr_sum.
        ops.append('-')
        self._search(num, target, idx + 1, 0, -1, curr_sum + curr_prod * curr_num, ops, results)
        ops.pop()
        # Case 4: *. Reset curr_num to 0. Aggregate curr_prod. Keep curr_sum.
        ops.append('*')
        self._search(num, target, idx + 1, 0, curr_prod * curr_num, curr_sum, ops, results)
        ops.pop()

    def addOperators(self, num: str, target: int) -> List[str]:
        if not num:
            return []
        curr_num = 0
        curr_prod = 1
        curr_sum = 0
        ops = []
        results = []
        self._search(num, target, 0, curr_num, curr_prod, curr_sum, ops, results)
        return results
