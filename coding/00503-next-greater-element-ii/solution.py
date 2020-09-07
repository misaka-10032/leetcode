#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        desc_stack = []
        next_greater = [-1] * len(nums)
        for i, v in enumerate(nums):
            while desc_stack and nums[desc_stack[-1]] < v:
                smaller_i = desc_stack.pop()
                next_greater[smaller_i] = i
            desc_stack.append(i)
        for i, v in enumerate(nums):
            if len(desc_stack) == 1:
                break
            while desc_stack and nums[desc_stack[-1]] < v:
                smaller_i = desc_stack.pop()
                next_greater[smaller_i] = i
        return [nums[i] if i >= 0 else -1 for i in next_greater]
