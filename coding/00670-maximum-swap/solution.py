#!/usr/bin/env python3
# encoding: utf-8


class Solution:
    def maximumSwap(self, num: int) -> int:
        num_chars = list(str(num))

        # Find a leading non-increasing sequence.
        leading_end_idx = 1
        while (leading_end_idx < len(num_chars) and
               num_chars[leading_end_idx] <= num_chars[leading_end_idx - 1]):
            leading_end_idx += 1
        if leading_end_idx == len(num_chars):
            return num

        # Find the max val after the leading sequence.
        non_leading_max_val = num_chars[leading_end_idx]
        non_leading_max_idx = leading_end_idx
        idx = non_leading_max_idx + 1
        while idx < len(num_chars):
            if num_chars[idx] >= non_leading_max_val:
                non_leading_max_val = num_chars[idx]
                non_leading_max_idx = idx
            idx += 1

        # Find the first element that is < non_leading_max_val
        idx = 0
        while idx < leading_end_idx:
            if num_chars[idx] < non_leading_max_val:
                num_chars[idx], num_chars[non_leading_max_idx] = (
                    num_chars[non_leading_max_idx], num_chars[idx])
                break
            idx += 1
        return int(''.join(num_chars))
