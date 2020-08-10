# Sliding Window Maximum

https://leetcode.com/problems/sliding-window-maximum/

## Solution

Maintain a special queue that has the following properties.

* The elements in the queue are strictly decreasing.
* The elements will be flushed if the timestamp passes its time-to-live.
