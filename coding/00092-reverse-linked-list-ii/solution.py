#!/usr/bin/env python3
# encoding: utf-8

from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_and_next(
    left: ListNode, right: ListNode
) -> Tuple[ListNode, Optional[ListNode]]:
    post_right = right.next
    right.next = left
    return right, post_right


class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre_left = dummy = ListNode(next=head)
        left = head
        for _ in range(m - 1):
            pre_left, left = left, left.next
        pre_init_left, init_left = pre_left, left
        right = left.next
        for _ in range(n - m):
            left, right = reverse_and_next(left, right)
        last_left, last_right = left, right
        pre_init_left.next, init_left.next = (
            last_left, last_right)
        return dummy.next
