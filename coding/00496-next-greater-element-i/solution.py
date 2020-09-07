#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        desc_stack2 = []
        next_greater2 = {}
        for v2 in nums2:
            while desc_stack2 and v2 > desc_stack2[-1]:
                smaller = desc_stack2.pop()
                next_greater2[smaller] = v2
            desc_stack2.append(v2)

        result = []
        for v1 in nums1:
            result.append(next_greater2.get(v1, -1))
        return result
