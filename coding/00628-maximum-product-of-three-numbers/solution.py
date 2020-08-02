#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def _prod(self, nums: List[int]) -> int:
        prod = 1
        for num in nums:
            prod *= num
        return prod

    def maximumProduct(self, nums: List[int]) -> int:
        # Let's discuss the cases for the candidates that make the biggest product.
        # + represents >= 0. - represents < 0.
        # Case 1: +++. The biggest is from sorted_nums[-3:]
        # Case 2: --+. The biggest is from (sorted_nums[:2] + sorted_nums[-1:])
        # Case 3: -++. The biggest is around the zero. However, if we have >= 2
        #   non-negative numbers, this case is impossible, because --+ must have made
        #   a bigger product. Otherwise, it happens to be the product of sorted_nums[-3:].
        # Case 4: ---. The biggest is near the zero. However, if we have >= 1
        #   positive numbers, this case is impossible, because we could have made
        #   a bigger product with --+. That said, nums must be all < 0 for this case
        #   to happen, and the biggest is from sorted_nums[-3:]
        # All the above cases have either candidates from sorted_nums[-3:], or from
        # (sorted_nums[:2] + sorted_nums[-1:]).
        sorted_nums = sorted(nums)
        return max(self._prod(sorted_nums[-3:]),
                   self._prod(sorted_nums[:2] + sorted_nums[-1:]))
