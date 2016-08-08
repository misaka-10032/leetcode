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
    def mergeTwoLists(self, l1, l2):
        """
        compare head of l1, l2
        be careful of edge cases:
        1. empty l1
        2. empty l2

        Be careful of alias.
        Because it's required to splice two list, the position
        to update p.next is tricky. It's easy to get into the
        "loop-back" situation.

        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1

        head = l1 if l1.val < l2.val else l2
        p = head
        while l1 and l2:
            if l1.val < l2.val:
                p_next = l1
                l1 = l1.next
                # l1 should go before p set its next
                p.next = p_next
                p = p.next
            else:
                p_next = l2
                l2 = l2.next
                # similar to l2
                p.next = p_next
                p = p.next

        if l1:
            p.next = l1
        else:
            p.next = l2

        return head
