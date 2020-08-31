#!/usr/bin/env python3
# encoding: utf-8

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next


class Solution:
    def _should_continue(self, left: 'Node', right: 'Node', node: 'Node',
                         circled_back: bool) -> bool:
        if left.val <= node.val <= right.val:
            return False
        if circled_back:
            return False
        if left.val > right.val:
            if node.val >= left.val or node.val <= right.val:
                return False
        return True

    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        node = Node(insertVal)
        if not head:
            node.next = node
            return node

        if head.next == head:
            head.next, node.next = node, head
            return head

        left, right = head, head.next
        circled_back = False
        while self._should_continue(left, right, node, circled_back):
            left, right = left.next, right.next
            if left == head:
                circled_back = True
        left.next, node.next = node, right
        return head
