#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import Deque, Dict, Tuple

DIRS = ((1, 2), (2, 1), (2, -1), (1, -2),
        (-1, -2), (-2, -1), (-2, 1), (-1, 2))


class Solution:

    def _probe(self, x_min: int, x_max: int, y_min: int, y_max: int,
               t_map: Dict[Tuple[int, int], int],
               s_map: Dict[Tuple[int, int], int],
               s_queue: Deque[Tuple[int, int]]) -> int:
        x_s, y_s = s_queue.popleft()
        d_s = s_map[(x_s, y_s)]
        for dx, dy in DIRS:
            x2, y2 = x_s + dx, y_s + dy
            if (x2, y2) in s_map:
                continue
            if (x2, y2) in t_map:
                return d_s + 1 + t_map[(x2, y2)]
            if x2 < x_min or x2 > x_max or y2 < y_min or y2 > y_max:
                continue
            s_map[(x2, y2)] = d_s + 1
            s_queue.append((x2, y2))
        return -1

    def minKnightMoves(self, x: int, y: int) -> int:
        if (x, y) == (0, 0):
            return 0
        x_min, x_max = min(0, x) - 2, max(0, x) + 2
        y_min, y_max = min(0, y) - 2, max(0, y) + 2
        s_map = {(0, 0): 0}
        s_queue = collections.deque(s_map)
        t_map = {(x, y): 0}
        t_queue = collections.deque(t_map)
        while s_queue or t_queue:
            if s_queue:
                maybe_steps = self._probe(x_min, x_max, y_min, y_max, t_map, s_map, s_queue)
                if maybe_steps > 0:
                    return maybe_steps
            if t_queue:
                maybe_steps = self._probe(x_min, x_max, y_min, y_max, s_map, t_map, t_queue)
                if maybe_steps > 0:
                    return maybe_steps
        return 0
