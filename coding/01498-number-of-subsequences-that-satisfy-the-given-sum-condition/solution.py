#!/usr/bin/env python3
# encoding: utf-8

from typing import List


def increment(cnt, delta):
    mod_base = (10 ** 9) + 7
    return (cnt + delta) % mod_base


def bin_search(nums, start, val):
    # Finds in nums[start:] the first element that is strictly greater val.
    # `start` is inclusive; `end` is exclusive. Returns the index of the
    # element. If not found, returns len(nums). Assumes `nums` is non-empty.
    end = len(nums)
    while start < end - 2:
        mid = (start + end) // 2
        mid_val = nums[mid]
        if mid_val <= val:
            start = mid + 1
        else:  # mid_val > val
            end = mid + 1

    for idx in range(start, end):
        if nums[idx] > val:
            return idx
    return end


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        cnt = 0
        nums = sorted(nums)
        left = right = 0
        while left < len(nums):
            # Left is inclusive. Right is exclusive.
            # sorted_num[left:right] == v
            v = nums[left]
            # Fix v as min. Early return if v is too big.
            if v + v > target:
                break

            # Find the right boundary (exclusive) of v.
            right = bin_search(nums, left, v)
            v_cnt = right - left
            # At least one v should appear in the v sequence.
            v_seq_cnt = (1 << v_cnt) - 1

            # Fix v as min, and find the upper bound (exclusive).
            ub = bin_search(nums, right, target - v)
            # The ub sequence can emit arbitrary elements.
            ub_seq_cnt = 1 << (ub - right)
            cnt = increment(cnt, v_seq_cnt * ub_seq_cnt)

            left = right
        return cnt
