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
    def removeNthFromEnd(self, head, n):
        """
        In order to do it in one pass, the head/tail pointer
        needs to be n elements away.

        Be careful of edge case.

        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        prev = None
        q = p = head
        for _ in xrange(n-1):
            p = p.next
        while p.next:
            p = p.next
            prev = q
            q = q.next
        if prev is None:
            head = q.next
        else:
            prev.next = q.next
        del q
        return head
