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

    def __eq__(self, other):
        return self.val == other.val


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        p = head
        if not p:
            return
        q = p.next
        if not q:
            return p
        r = q.next

        p.next = None
        while r:
            q.next = p
            p, q, r = q, r, r.next
        q.next = p
        return q
