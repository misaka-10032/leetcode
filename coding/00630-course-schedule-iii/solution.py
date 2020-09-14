#!/usr/bin/env python3
# encoding: utf-8

import heapq
from typing import List


class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses = sorted(courses, key=lambda p: p[1])
        start = 1
        heap = []
        for duration, max_end in courses:
            if duration > max_end:
                continue
            end = start + duration - 1
            if end <= max_end:
                heapq.heappush(heap, -duration)
                start += duration
                continue
            max_duration = -heap[0]
            if duration >= max_duration:
                continue
            end = start - max_duration + duration - 1
            if end <= max_end:
                heapq.heapreplace(heap, -duration)
                start = end + 1
        return len(heap)
