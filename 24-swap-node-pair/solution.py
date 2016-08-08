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
    def swapPairs(self, head):
        """
        two probes, a pre
        edge case:
          y
          x->x...->x->x->y
        :type head: ListNode
        :rtype: ListNode
        """
        # 0 node
        if not head:
            return None

        # 1 node
        if not head.next:
            return head

        # >=2 nodes
        pre = ListNode(None)  # dummy pre
        q = head
        p = head.next
        head = p

        while p.next and p.next.next:
            n1, n2 = p.next, p.next.next
            pre.next = p
            p.next = q
            q.next = n1
            pre, q, p = q, n1, n2

        # if last 1 is dangling, q, p are not yet swapped.
        if p.next and not p.next.next:
            last = p.next
            pre.next = p
            p.next = q
            q.next = last
            last.next = None
        # otherwise last 2 are dangling
        else:
            pre.next = p
            p.next = q
            q.next = None

        return head
