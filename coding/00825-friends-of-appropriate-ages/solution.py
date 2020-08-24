#!/usr/bin/env python3
# encoding: utf-8

import collections
from typing import List


class Solution:
    def _follows(self, age1: int, age2: int) -> True:
        if age2 <= 0.5 * age1 + 7:
            return False
        if age2 > age1:
            return False
        if age2 > 100 and age1 < 100:
            return False
        return True

    def numFriendRequests(self, ages: List[int]) -> int:
        age_counter = collections.Counter(ages)
        cnt = 0
        for age1, cnt1 in age_counter.items():
            for age2, cnt2 in age_counter.items():
                if age1 == age2:
                    if cnt1 > 1:
                        if self._follows(age1, age1):
                            cnt += cnt1 * (cnt1 - 1)
                else:
                    if self._follows(age1, age2):
                        cnt += cnt1 * cnt2
        return cnt
