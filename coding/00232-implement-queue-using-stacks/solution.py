#!/usr/bin/env python3
# encoding: utf-8


class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._input_stack = []
        self._output_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._input_stack.append(x)

    def _maybe_prepare_output_stack(self):
        if self._output_stack:
            return
        while self._input_stack:
            self._output_stack.append(self._input_stack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self._maybe_prepare_output_stack()
        return self._output_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self._maybe_prepare_output_stack()
        return self._output_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._input_stack and not self._output_stack
