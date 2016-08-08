# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeKLists(self, lists):
        """
        Boring.
        Just use list then sort it.
        Heap would be slower, because every time it needs
        to sift down from top.

        :type lists: List[ListNode]
        :rtype: ListNode
        """
        all = []
        # lists = list(lists)  # copy if necessary
        for lst in lists:
            while lst:
                all.append(lst)
                lst = lst.next

        all = sorted(all, key=lambda node: node.val)
        if not all:
            return None

        head = all[0]
        head.next = None
        prev = node = head
        for i in xrange(1, len(all)):
            node = all[i]
            prev.next = node
            prev = node
        node.next = None

        return head
