#!/usr/bin/env python3
# encoding: utf-8

import dataclasses
from typing import Set


@dataclasses.dataclass
class Node:
    cnt: int
    keys: Set[str] = dataclasses.field(default_factory=set)
    prev: 'Node' = None
    next: 'Node' = None


class AllOne:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dummy_node = Node(0)
        self._max_node = self._dummy_node
        self._key_to_node_map = {}

    def _insert_node(self, new_node: Node, after_node: Node):
        # After insertion, it will be after_node <-> new_node <-> after_node2.
        # after_node2 can be None.
        after_node2 = after_node.next
        after_node.next = new_node
        new_node.prev, new_node.next = after_node, after_node2
        if after_node2:
            after_node2.prev = new_node

    def _remove_node(self, node: Node):
        # After removal, it will be prev_node <-> next_node.
        # next_node can be None.
        prev_node, next_node = node.prev, node.next
        prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node

    def _get_or_create_next_node(self, node: Node) -> Node:
        maybe_next_node = node.next
        if node.next and node.next.cnt == node.cnt + 1:
            next_node = node.next
        else:
            next_node = Node(node.cnt + 1)
            self._insert_node(next_node, node)
        return next_node

    def _move_key_to_next_node(self, key: str, node: Node):
        next_node = self._get_or_create_next_node(node)
        next_node.keys.add(key)
        self._key_to_node_map[key] = next_node

        node.keys.remove(key)
        if not node.keys and node is not self._dummy_node:
            self._remove_node(node)

        if node is self._max_node:
            self._max_node = next_node

    def inc(self, key: str) -> None:
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        maybe_node = self._key_to_node_map.get(key, None)
        if maybe_node:
            node = maybe_node
        else:
            node = self._dummy_node
            node.keys.add(key)
        self._move_key_to_next_node(key, node)

    def _get_or_create_prev_node(self, node: Node) -> Node:
        assert node.prev
        if node.prev.cnt == node.cnt - 1:
            prev_node = node.prev
        else:
            prev_node = Node(node.cnt - 1)
            self._insert_node(prev_node, node.prev)
        return prev_node

    def _move_key_to_prev_node(self, key: str, node: Node):
        prev_node = self._get_or_create_prev_node(node)
        if prev_node is self._dummy_node:
            self._key_to_node_map.pop(key)
        else:
            prev_node.keys.add(key)
            self._key_to_node_map[key] = prev_node

        node.keys.remove(key)
        if not node.keys:
            self._remove_node(node)

        if node is self._max_node and not node.keys:
            self._max_node = prev_node
            prev_node.next = None

    def dec(self, key: str) -> None:
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        maybe_node = self._key_to_node_map.get(key, None)
        if not maybe_node:
            return
        node = maybe_node
        self._move_key_to_prev_node(key, node)

    def getMaxKey(self) -> str:
        """
        Returns one of the keys with maximal value.
        """
        for key in self._max_node.keys:
            return key
        return ''

    def getMinKey(self) -> str:
        """
        Returns one of the keys with Minimal value.
        """
        min_node = self._dummy_node.next
        if not min_node:
            return ''
        for key in min_node.keys:
            return key

# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
