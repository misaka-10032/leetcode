#!/usr/bin/env python3
# encoding: utf-8

import heapq
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ComparableListNode:
    def __init__(self, node: ListNode):
        self.node = node

    def __lt__(self, other):
        return self.node.val < other.node.val

    def __gt__(self, other):
        return self.node.val > other.node.val

    def __eq__(self, other):
        return self.node.val == other.node.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        iters: List[ComparableListNode] = []
        for it in lists:
            if it is not None:
                iters.append(ComparableListNode(it))
        heapq.heapify(iters)

        it = dummy = ListNode()
        while iters:
            it_in: ComparableListNode = heapq.heappop(iters)
            it.next = it_in.node
            it = it.next
            it_in.node = it_in.node.next
            if it_in.node is not None:
                heapq.heappush(iters, it_in)
        return dummy.next
