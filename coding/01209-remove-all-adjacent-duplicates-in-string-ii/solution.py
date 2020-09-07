#!/usr/bin/env python3
# encoding: utf-8

import dataclasses


@dataclasses.dataclass
class Node:
    char: str
    cnt: int = 1


class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for char in s:
            if stack:
                if stack[-1].char == char:
                    if stack[-1].cnt == k-1:
                        stack.pop()
                    else:
                        stack[-1].cnt += 1
                else:
                    stack.append(Node(char))
            else:
                stack.append(Node(char))
        return ''.join(map(lambda n: n.char * n.cnt, stack))
