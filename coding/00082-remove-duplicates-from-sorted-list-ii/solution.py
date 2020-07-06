#!/usr/bin/env python3
# encoding: utf-8


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def find_next_dup(pre_left):
    post_right = left = pre_left.next
    while left is not None:
        cnt = 0
        while post_right is not None and post_right.val == left.val:
            cnt += 1
            post_right = post_right.next
        if cnt > 1:
            break
        pre_left, left = left, post_right
    return pre_left, left, post_right


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pre_left = dummy = ListNode(next=head)
        while True:
            pre_left, left, post_right = find_next_dup(pre_left)
            if left is None:
                break
            pre_left.next = post_right
        return dummy.next
