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
        def _reverse(p, q):
            if q:
                head = _reverse(q, q.next)
                q.next = p
                return head
            return p
        return _reverse(None, head)
