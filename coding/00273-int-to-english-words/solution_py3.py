#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Solution:
    def break_num_to_thousands(self, num: int) -> List[int]:
        # Returns a group of int's, representing billions,
        # millions, thousands, and hundreds.
        nums = [0] * 4
        for i in range(3, -1, -1):
            nums[i] = num % 1000
            num //= 1000
        assert num == 0
        return nums

    def read_lt_10(self, num: int) -> str:
        assert num < 10
        texts = [
            '', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine'
        ]
        return texts[num]

    def read_lt_20(self, num: int) -> str:
        assert num < 20
        texts = [
            'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen',
            'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
        ]
        if num < 10:
            return self.read_lt_10(num)
        else:
            return texts[num - 10]

    def read_ge_20_lt_100(self, num: int) -> str:
        assert 20 <= num < 100
        texts = [
            'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety'
        ]
        tens = num // 10
        rest = num % 10
        result = [texts[tens - 2]]
        if rest > 0:
            result.append(self.read_lt_10(rest))
        return ' '.join(result)

    def read_lt_100(self, num: int) -> str:
        assert num < 100
        if num < 20:
            return self.read_lt_20(num)
        elif num < 100:
            return self.read_ge_20_lt_100(num)

    def read_ge_100_lt_1000(self, num: int) -> str:
        assert 100 <= num < 1000
        hundreds = num // 100
        rest = num % 100
        result = [self.read_lt_10(hundreds), 'Hundred']
        if rest > 0:
            result.append(self.read_lt_100(rest))
        return ' '.join(result)

    def read_lt_1000(self, num: int) -> str:
        assert num < 1000
        if num < 100:
            return self.read_lt_100(num)
        else:
            return self.read_ge_100_lt_1000(num)

    def chain_up_thousands(self, nums: List[int]) -> str:
        assert len(nums) == 4
        suffixes = ['Billion', 'Million', 'Thousand', '']
        text = []
        for num, suffix in zip(nums, suffixes):
            if num:
                text.append(self.read_lt_1000(num))
                if suffix:
                    text.append(suffix)
        return ' '.join(text)

    def numberToWords(self, num: int) -> str:
        if num == 0:
            return 'Zero'
        nums = self.break_num_to_thousands(num)
        return self.chain_up_thousands(nums)
