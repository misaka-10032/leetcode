# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).
All rights reserved.

"""
__author__ = 'misaka-10032'


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        """ pseudo-root """
        l = ListNode(None)
        """ previous """
        q = l
        """ p is probe, carry is carry. """
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + carry
            carry = val // 10
            val %= 10
            p = ListNode(val)
            q.next = p
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            q = p

        return l.next
