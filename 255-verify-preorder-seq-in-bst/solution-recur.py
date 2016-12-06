# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* First is root
* Two chunks are the two subtrees
* First chunk is all < root
* Second chunk are all > root
"""


class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """

        def verify(left, right):
            """ verify [left, right) of preorder """
            if left == right:
                return True
            root = preorder[left]

            i = left + 1
            while i < right and preorder[i] < root:
                i += 1
            if not verify(left + 1, i):
                return False

            k = i
            while i < right and preorder[i] > root:
                i += 1
            return i == right and verify(k, right)

        return verify(0, len(preorder))
