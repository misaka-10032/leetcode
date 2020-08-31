#!/usr/bin/env python3
# encoding: utf-8

# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def _find_first_with_child_or_last_node(self, node: 'Node') -> 'Node':
        while True:
            if node.child:
                return node
            if not node.next:
                return node
            node = node.next
        return None

    def _traverse(self, node: 'Node') -> 'Node':
        while True:
            node = self._find_first_with_child_or_last_node(node)
            if not node.child:
                return node
            next_node = node.next
            child_node = node.child
            node.next, child_node.prev = child_node, node
            last_child_node = self._traverse(child_node)
            node.child = None
            if not next_node:
                return last_child_node
            last_child_node.next, next_node.prev = next_node, last_child_node
            node = next_node

    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return None
        self._traverse(head)
        return head
