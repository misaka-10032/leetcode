#!/usr/bin/env python3
# encoding: utf-8

import dataclasses
from typing import Union


@dataclasses.dataclass
class KvNode:
    key: int
    val: int
    freq_node: 'FreqNode' = None
    prev: 'KeyNode' = None
    next: 'KeyNode' = None


@dataclasses.dataclass
class FreqNode:
    freq: int
    kv_node_list: 'LinkedList' = dataclasses.field(
        default_factory=lambda: LinkedList(KvNode('', -1)))
    prev: 'FreqNode' = None
    next: 'FreqNode' = None


class LinkedList:

    def __init__(self, head: Union[KvNode, FreqNode]):
        self.head = head
        self.tail = head

    def add(self, node: Union[KvNode, FreqNode],
            after_node: Union[KvNode, FreqNode] = None):
        if not after_node:
            after_node = self.tail
        next_after_node = after_node.next
        after_node.next, node.prev = node, after_node
        node.next = next_after_node
        if next_after_node:
            next_after_node.prev = node
        if after_node is self.tail:
            self.tail = node

    def remove(self, node: Union[KvNode, FreqNode]):
        prev_node, next_node = node.prev, node.next
        node.prev = node.next = None
        prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        if node is self.tail:
            self.tail = prev_node

    def empty(self) -> bool:
        return self.head.next is None


class LFUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._key_to_kv_node_map = {}
        self._freq_node_list = LinkedList(FreqNode(0))

    def _get_or_create_next_freq_node(self, freq_node: FreqNode) -> FreqNode:
        if freq_node.next and freq_node.next.freq == freq_node.freq + 1:
            return freq_node.next
        next_freq_node = FreqNode(freq_node.freq + 1)
        self._freq_node_list.add(next_freq_node, freq_node)
        return next_freq_node

    def get(self, key: int) -> int:
        kv_node = self._key_to_kv_node_map.get(key, None)
        if not kv_node:
            return -1

        freq_node = kv_node.freq_node
        next_freq_node = self._get_or_create_next_freq_node(freq_node)
        freq_node.kv_node_list.remove(kv_node)
        if freq_node.kv_node_list.empty():
            self._freq_node_list.remove(freq_node)
        next_freq_node.kv_node_list.add(kv_node)
        kv_node.freq_node = next_freq_node
        return kv_node.val

    def put(self, key: int, value: int) -> None:
        if self._capacity <= 0:
            return

        # Find the KvNode
        kv_node = self._key_to_kv_node_map.get(key, None)
        # If any, update the value and call get() to update frequency.
        if kv_node:
            kv_node.val = value
            self.get(key)
            return

        # If the capacity is reached, pop the least frequent and the least
        # recent node.
        if len(self._key_to_kv_node_map) == self._capacity:
            freq_node = self._freq_node_list.head.next
            kv_node = freq_node.kv_node_list.head.next
            freq_node.kv_node_list.remove(kv_node)
            self._key_to_kv_node_map.pop(kv_node.key)
            if freq_node.kv_node_list.empty():
                self._freq_node_list.remove(freq_node)

        # Otherwise, create one.
        kv_node = KvNode(key, value)
        self._key_to_kv_node_map[key] = kv_node
        # See if there is 1-freq node. If there is, insert the node there.
        # Otherwise, create one and insert there.
        freq_node = self._get_or_create_next_freq_node(self._freq_node_list.head)
        freq_node.kv_node_list.add(kv_node)
        kv_node.freq_node = freq_node

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
