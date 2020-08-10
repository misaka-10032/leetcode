# encoding: utf-8
"""
Created by misaka-10032 (longqic@andrew.cmu.edu).

* Use stack
* Cares about the v-shape
* ignore the initial climbing like /
* while dropping like \, push index into stack
  * keep pushing when height is strictly decreasing
* while climbing
  * pop until val of heap top is strictly greater the current val.
  * While popping, accumulate the water volume.
  * Popping it is like fill the space with solid stage.
* Finally, push the new stage into stack
* Be careful how to compute the gap and the height of the current strip of water.
  * gap between `i` and `j` is `j-i-1`
  * strip height is `h[j] - prev`
  * prev starts with 0, and becomes h[j] while popping.
* Edge case:
  * After popping, if stack is not empty yet, we need to compute the final strip
    from right to left, like this
    __
      |  _
      |_| |
  * Gap size is computed the same
  * Strip height is `h[i] - prev` (now it's `i`).
"""

from collections import deque


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        stack = deque()
        i = 0
        v = 0
        while i < n:
            while i < n and (not stack or height[i] < height[stack[-1]]):
                stack.append(i)
                i += 1
            prev = 0
            while stack and i < n and height[i] >= height[stack[-1]]:
                j = stack.pop()
                v += (i-j-1) * (height[j]-prev)
                prev = height[j]
            if stack and i < n:
                j = stack[-1]
                v += (i-j-1) * (height[i]-prev)
        return v
