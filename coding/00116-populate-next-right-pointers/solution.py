#!/usr/bin/env python3
# encoding: utf-8

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        probe = head = root
        while probe:
            while probe:
                if probe.left and probe.right:
                    probe.left.next = probe.right
                    if probe.next:
                        probe.right.next = probe.next.left
                probe = probe.next
            probe = head = head.left
        return root
