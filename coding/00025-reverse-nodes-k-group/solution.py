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
    def reverse_group(self, start, end):
        q, p = None, start
        while p is not end:
            p_next = p.next
            p.next = q
            q, p = p, p_next
        if p is not None:
            p.next = q

    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None:
            return None

        p = head
        # try first k. probe edge case
        cnt = 0
        while p:
            cnt += 1
            if cnt >= k:
                break
            p = p.next

        # edge case: n < k
        if not p:
            return head

        pre_next, p_next = head, p.next
        self.reverse_group(head, p)
        head = p

        while True:
            pre = pre_next
            q = p = p_next
            # probe group end
            cnt = 0
            while p:
                cnt += 1
                if cnt >= k:
                    break
                p = p.next

            # ignore residue
            if not p:
                # connect group
                pre.next = q
                break

            # connect group, the next group head changes
            pre.next = p
            # preserve p_next before reverse inside
            p_next = p.next
            self.reverse_group(q, p)
            # prepare next
            pre_next = q

        return head
