# Simplify Path

https://leetcode.com/problems/simplify-path/

## Solution

Use a stack to track the current path. Here are two possible traps:

* '..' at the root should be a no-op.
* If the result is '/', the component stack is empty, and a regular `join()` won't work.
