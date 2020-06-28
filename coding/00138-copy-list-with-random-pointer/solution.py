# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return

        head_copy = RandomListNode(head.label)
        old_to_new = {head: head_copy}
        p = head.next
        prev_copy = head_copy
        while p:
            p_copy = RandomListNode(p.label)
            old_to_new[p] = p_copy
            prev_copy.next = p_copy
            prev_copy = p_copy
            p = p.next

        p = head
        p_copy = head_copy
        while p:
            if p.random:
                p_copy.random = old_to_new[p.random]
            p = p.next
            p_copy = p_copy.next
        return head_copy
