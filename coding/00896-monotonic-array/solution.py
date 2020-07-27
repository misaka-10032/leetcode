#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_increase = True
        for i in range(1, len(A)):
            if A[i] < A[i-1]:
                is_increase = False
                break
        if is_increase:
            return True
        for i in range(1, len(A)):
            if A[i] > A[i-1]:
                return False
        return True
