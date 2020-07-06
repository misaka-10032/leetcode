#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Tuple, Union


class Solution:
    def eval_postfix(self, postfix: List[Union[int, str]]) -> int:
        num_stack = []
        op_to_fn = {
            '+': lambda v1, v2: v1 + v2,
            '-': lambda v1, v2: v1 - v2,
            '*': lambda v1, v2: v1 * v2,
            '/': lambda v1, v2: v1 // v2,
        }
        for curr_item in postfix:
            if isinstance(curr_item, int):
                num_stack.append(curr_item)
            else:
                v2 = num_stack.pop()
                v1 = num_stack.pop()
                num_stack.append(op_to_fn[curr_item](v1, v2))
        return num_stack.pop() if num_stack else 0

    def parse_next(self, infix: str, idx: int) -> Tuple[Union[None, int, str], int]:
        while idx != len(infix) and infix[idx] == ' ':
            idx += 1
        if idx == len(infix):
            return None, idx
        elif infix[idx].isdigit():
            num = 0
            while idx != len(infix) and infix[idx].isdigit():
                num = num * 10 + ord(infix[idx]) - ord('0')
                idx += 1
            return num, idx
        else:
            return infix[idx], idx + 1

    def infix_to_postfix(self, infix: str) -> List[Union[int, str]]:
        precedence = {'(': 0, '+': 1, '-': 1, '*': 2, '/': 2}
        idx = 0
        postfix = []
        op_stack = []
        prev_is_num = False
        num_is_negative = False
        while idx != len(infix):
            item, next_idx = self.parse_next(infix, idx)
            if item is None:
                break
            elif isinstance(item, int):
                if num_is_negative:
                    item = -item
                    num_is_negative = False
                postfix.append(item)
                prev_is_num = True
            elif item == '(':
                op_stack.append(item)
                prev_is_num = False
            elif item == ')':
                while op_stack[-1] != '(':
                    postfix.append(op_stack.pop())
                op_stack.pop()
                prev_is_num = True
            else:  # item in ('+', '-', '*', '/')
                if prev_is_num:
                    curr_precedence = precedence[item]
                    while op_stack and precedence[op_stack[-1]] >= curr_precedence:
                        postfix.append(op_stack.pop())
                    op_stack.append(item)
                    prev_is_num = False
                else:
                    if item == '-':
                        num_is_negative = not num_is_negative
            idx = next_idx
        while op_stack:
            postfix.append(op_stack.pop())
        return postfix

    def calculate(self, s: str) -> int:
        postfix = self.infix_to_postfix(s)
        return self.eval_postfix(postfix)
