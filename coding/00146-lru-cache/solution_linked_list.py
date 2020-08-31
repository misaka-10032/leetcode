#!/usr/bin/env python3
# encoding: utf-8

import dataclasses
from typing import Optional


@dataclasses.dataclass
class Node:
    key: int
    val: int
    next: Optional['Node'] = None
    prev: Optional['Node'] = None


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._head_node = Node('__head__', -1)
        self._tail_node = self._head_node
        self._key_to_node_map = {}

    def _remove_node(self, node: Node):
        if node is self._tail_node:
            self._tail_node = node.prev
        pre_node = node.prev
        post_node = node.next
        pre_node.next = post_node
        if post_node:
            post_node.prev = pre_node

    def _insert_node_to_tail(self, node: Node):
        self._tail_node.next, node.prev, node.next = (
            node, self._tail_node, None)
        self._tail_node = node

    def _refresh_node(self, node: Node):
        self._remove_node(node)
        self._insert_node_to_tail(node)

    def get(self, key: int) -> int:
        maybe_node = self._key_to_node_map.get(key, None)
        if not maybe_node:
            return -1
        self._refresh_node(maybe_node)
        return maybe_node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity <= 0:
            return

        maybe_node = self._key_to_node_map.get(key, None)
        if maybe_node:
            maybe_node.val = value
            self._refresh_node(maybe_node)
            return

        if len(self._key_to_node_map) == self._capacity:
            first_node = self._head_node.next
            if first_node:
                self._remove_node(first_node)
                self._key_to_node_map.pop(first_node.key)

        node = Node(key, value)
        self._insert_node_to_tail(node)
        self._key_to_node_map[key] = node
