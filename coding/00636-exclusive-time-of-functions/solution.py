#!/usr/bin/env python3
# encoding: utf-8

import dataclasses
from typing import List


@dataclasses.dataclass
class LogItem:
    func_id: int
    event: str
    # For the start time, it's the start of the timestamp. However, for the end time,
    # we set this number to be the start of the *next* timestamp.
    ts: int


class Solution:

    def _parse_log(self, log: str) -> LogItem:
        items = log.split(':')
        event = items[1]
        ts = int(items[2])
        if event == 'end':
            ts += 1
        return LogItem(int(items[0]), event, ts)

    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        # Maintain a stack of logs and a stack of wait times.
        durations = [0] * n
        log_stack = [None]
        wait_time_stack = [0]
        for log in logs:
            log_item = self._parse_log(log)
            if log_item.event == 'start':
                log_stack.append(log_item)
                wait_time_stack.append(0)
            else:
                popped_log_item = log_stack.pop()
                popped_wait_time = wait_time_stack.pop()
                assert popped_log_item.event == 'start'
                assert popped_log_item.func_id == log_item.func_id
                popped_duration = log_item.ts - popped_log_item.ts
                wait_time_stack[-1] += popped_duration
                durations[log_item.func_id] += popped_duration - popped_wait_time
        return durations
