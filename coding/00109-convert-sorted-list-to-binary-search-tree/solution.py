#!/usr/bin/env python3
# encoding: utf-8

from typing import Optional, Tuple


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def find_mid(head: ListNode, cnt: int) -> Tuple[ListNode, int, int]:
    mid_idx = cnt // 2
    mid = head
    for _ in range(mid_idx):
        mid = mid.next
    left_cnt = mid_idx
    right_cnt = cnt - left_cnt - 1
    return mid, left_cnt, right_cnt


def build_bst(
    head: Optional[ListNode], cnt: int
) -> Optional[TreeNode]:
    if head is None or cnt == 0:
        return None
    mid, left_cnt, right_cnt = find_mid(head, cnt)
    root = TreeNode(val=mid.val)
    root.left = build_bst(head, left_cnt)
    root.right = build_bst(mid.next, right_cnt)
    return root


class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        it = head
        cnt = 0
        while it is not None:
            it = it.next
            cnt += 1
        return build_bst(head, cnt)
