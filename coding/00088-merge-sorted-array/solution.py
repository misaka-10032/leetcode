#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        p1 = m - 1
        p2 = n - 1
        q = m + n - 1
        while p2 >= 0:
            num2 = nums2[p2]
            num1 = nums1[p1] if p1 >= 0 else (num2 - 1)
            if num1 > num2:
                nums1[q] = num1
                p1 -= 1
            else:
                nums1[q] = num2
                p2 -= 1
            q -= 1
