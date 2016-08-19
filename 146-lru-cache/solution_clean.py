# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

TODO: purpose
"""


class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None


class LRUCache(object):
    def __init__(self, capacity):
        """
        dict maps from key to node
        nodes form a doubly linked list
        lru <-> ... <-> mru

        :type capacity: int
        """
        self.kv = {}
        self.sz = 0
        self.cap = capacity
        self.lru = self.mru = None

    def _insert(self, node):
        if not self.lru and not self.mru:
            self.lru = self.mru = node
            return

        old_mru = self.mru
        old_mru.next = node
        node.prev = old_mru
        node.next = None
        self.mru = node

    def _remove(self, node):
        if not node:
            return
        if node is self.lru:
            self.lru = self.lru.next
        if node is self.mru:
            self.mru = self.mru.prev

        prev = node.prev
        next = node.next
        if prev:
            prev.next = next
        if next:
            next.prev = prev

    def get(self, key):
        """
        :rtype: int
        """
        if key not in self.kv:
            return -1
        node = self.kv[key]
        self._remove(node)
        self._insert(node)
        return node.val

    def set(self, key, val):
        """
        :type key: int
        :type val: int
        :rtype: nothing
        """
        if self.cap <= 0:
            return

        if key in self.kv:
            node = self.kv[key]
            node.val = val
            self._remove(node)
            self._insert(node)
            return

        node = Node(key, val)
        self.kv[key] = node

        if not self.lru and not self.mru:
            """ Init """
            self.lru = self.mru = node
        else:
            """ Add to end """
            self.mru.next = node
            node.prev = self.mru
            self.mru = node

        self.sz += 1
        if self.sz > self.cap:
            """ Evict """
            old_lru = self.lru
            new_lru = old_lru.next
            new_lru.prev = None
            self.lru = new_lru
            self.kv.pop(old_lru.key)
            self.sz -= 1
