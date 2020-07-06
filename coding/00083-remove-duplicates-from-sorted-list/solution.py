#!/usr/bin/env python3
# encoding: utf-8

from typing import Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_next_dup(pre_left: ListNode) -> Tuple[ListNode, ListNode]:
    left = post_right = pre_left.next
    while left is not None:
        cnt = 0
        while post_right is not None and post_right.val == left.val:
            cnt += 1
            post_right = post_right.next
        if cnt > 1:
            break
        left = post_right
    return left, post_right


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        left = dummy = ListNode(next=head)
        while True:
            left, post_right = find_next_dup(left)
            if left is None:
                return dummy.next
            left.next = post_right
