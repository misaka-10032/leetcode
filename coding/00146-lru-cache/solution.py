#!/usr/bin/env python3
# encoding: utf-8

import collections


class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._ordered_dict = collections.OrderedDict()

    def get(self, key: int) -> int:
        maybe_val = self._ordered_dict.pop(key, None)
        if maybe_val is None:
            return -1
        self._ordered_dict[key] = maybe_val
        return maybe_val

    def put(self, key: int, value: int) -> None:
        if self._capacity <= 0:
            return

        maybe_old_val = self._ordered_dict.pop(key, None)
        if maybe_old_val is not None:
            self._ordered_dict[key] = value
            return

        if len(self._ordered_dict) == self._capacity:
            self._ordered_dict.popitem(last=False)
        self._ordered_dict[key] = value
