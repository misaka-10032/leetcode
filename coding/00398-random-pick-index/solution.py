#!/usr/bin/env python3
# encoding: utf-8

import random
from typing import List


class Solution:

    def __init__(self, nums: List[int]):
        self._val_to_indices_map = {}
        for idx, v in enumerate(nums):
            if v in self._val_to_indices_map:
                ids = self._val_to_indices_map[v]
            else:
                ids = self._val_to_indices_map[v] = []
            ids.append(idx)

    def pick(self, target: int) -> int:
        ids = self._val_to_indices_map[target]
        id_idx = random.randrange(0, len(ids))
        return ids[id_idx]
