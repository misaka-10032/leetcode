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
        1. find total length
        2. compute the exact index in order
        3. edge case
          3.1 start/end
          3.2 empty list
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        # just in case
        if head is None:
            return None

        # 1st pass, get len
        l = 0
        p = head
        while p:
            p = p.next
            l += 1

        # kth in order
        k = l - n

        i = 0
        prev = None
        p = head
        # 2nd pass, find kth
        while p:
            if i == k:
                break
            prev = p
            p = p.next
            i += 1

        if prev is None:
            head = p.next
        else:
            prev.next = p.next

        return head
