#!/usr/bin/env python3
# encoding: utf-8

from typing import Dict, List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_to_cnt_map: Dict[str, int] = {}
        max_cnt = 0
        total_cnt = 0
        for task in tasks:
            total_cnt += 1
            task_cnt = task_to_cnt_map.get(task, 0)
            task_cnt += 1
            task_to_cnt_map[task] = task_cnt
            max_cnt = max(max_cnt, task_cnt)
        max_cnt_tasks = 0
        for task, cnt in task_to_cnt_map.items():
            if cnt == max_cnt:
                max_cnt_tasks += 1
        rest_cnt = total_cnt - max_cnt * max_cnt_tasks
        groups = max_cnt - 1
        empty_slots_per_group = max(0, n - max_cnt_tasks + 1)
        empty_slots = groups * empty_slots_per_group
        # Squeeze in the rest of the tasks
        empty_slots = max(0, empty_slots - rest_cnt)
        return empty_slots + total_cnt
