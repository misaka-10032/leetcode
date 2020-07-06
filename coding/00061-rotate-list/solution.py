#!/usr/bin/env python3
# encoding: utf-8


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_len(head: ListNode):
    it = head
    cnt = 0
    while it is not None:
        it = it.next
        cnt += 1
    return cnt


def move_to_last_k(head: ListNode, k: int):
    init_last = pre_first = ListNode(next=head)
    for _ in range(k):
        init_last = init_last.next
    while init_last.next is not None:
        pre_first = pre_first.next
        init_last = init_last.next
    return pre_first, pre_first.next, init_last


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        n = get_len(head)
        if n == 0:
            return None
        k = k % n
        if k == 0:
            return head
        init_first = head
        pre_first, first, init_last = move_to_last_k(head, k)
        pre_first.next, init_last.next = None, init_first
        return first
