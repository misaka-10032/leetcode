#!/usr/bin/env python3
# encoding: utf-8

import dataclasses
from typing import List


@dataclasses.dataclass
class Elevation:
    right: int
    top: int
    delta: int


class Solution:
    def trap(self, height: List[int]) -> int:
        # Maintain a stack of effective elevations. When a new elevation
        # is flat, we update the right boundary of the last elevation.
        # When a new elevation decreases in height, we push it to the stack.
        # When a new elevation increases in height, we pop until the top of
        # the stack has higher elevation. In the mean time, we aggregate the
        # water that we have raised.
        stack = []
        tot = 0
        for left, top in enumerate(height):
            right = left + 1
            if not stack:
                stack.append(Elevation(right, top, top))
                continue

            if top == stack[-1].top:
                stack[-1].right = right
            elif top < stack[-1].top:
                stack[-1].delta = stack[-1].top - top
                stack.append(Elevation(right, top, top))
            else:  # top >= stack[-1].top
                while stack and top >= stack[-1].top:
                    prev = stack.pop()
                    tot += (left - prev.right) * prev.delta
                if stack:
                    delta = top - (stack[-1].top - stack[-1].delta)
                    tot += (left - stack[-1].right) * delta
                    stack[-1].delta = stack[-1].top - top
                stack.append(Elevation(right, top, top))
        return tot
