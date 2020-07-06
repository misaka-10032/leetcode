#!/usr/bin/env python3
# encoding: utf-8

from typing import Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def move_k(pre_left: ListNode, k: int):
    for _ in range(k):
        if pre_left is not None:
            pre_left = pre_left.next
        else:
            return None
    return pre_left


def swap(left: ListNode, right: ListNode) -> Tuple[ListNode, ListNode]:
    next_right = right.next
    right.next = left
    return right, next_right


def swap_k(pre_left: ListNode, k: int):
    left = init_left = pre_left.next
    if left is None:
        return
    right = left.next
    for _ in range(k-1):
        if right is None:
            break
        left, right = swap(left, right)
    # last_right, last_next_right = left, right
    pre_left.next, init_left.next = left, right


class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        pre_left = dummy = ListNode(next=head)
        while pre_left is not None:
            if move_k(pre_left, k) is not None:
                swap_k(pre_left, k)
            pre_left = move_k(pre_left, k)
        return dummy.next
