#!/usr/bin/env python3
# encoding: utf-8

from typing import Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def rotate_and_move_forward(
    pre_left: ListNode, left: ListNode, pre_right: ListNode, right: ListNode
) -> Tuple[ListNode, ListNode, ListNode, ListNode]:
    post_right = right.next
    pre_left.next, pre_right.next, right.next = (
        right, post_right, left)
    return right, left, pre_right, post_right


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        pre_it_ge = dummy = ListNode(next=head)
        it_ge = head
        while it_ge is not None and it_ge.val < x:
            pre_it_ge, it_ge = it_ge, it_ge.next
        pre_it_lt = it_lt = it_ge
        while it_lt is not None:
            while it_lt is not None and it_lt.val >= x:
                pre_it_lt, it_lt = it_lt, it_lt.next
            if it_lt is None:
                break
            pre_it_ge, it_ge, pre_it_lt, it_lt = rotate_and_move_forward(
                pre_it_ge, it_ge, pre_it_lt, it_lt)
        return dummy.next
