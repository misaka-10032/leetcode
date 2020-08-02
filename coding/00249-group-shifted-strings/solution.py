#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import List, Optional, Tuple


class Solution:

    def _get_repr(self, string: str) -> Optional[Tuple[int, ...]]:
        if not string:
            return None
        result = []
        for i in range(1, len(string)):
            ord_0 = ord(string[0])
            ord_i = ord(string[i])
            result.append((ord_i - ord_0) % 26)
        return tuple(result)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        repr_to_strs_map = collections.defaultdict(list)
        for string in strings:
            my_repr = self._get_repr(string)
            repr_to_strs_map[my_repr].append(string)
        return list(repr_to_strs_map.values())
