# Read N Characters Given Read4 II - Call multiple times

https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/

## Solution

Keep the following until `_read_local()` returns a short read.

* `_maybe_read4()`: Update the local buffer if its all consumed.
* `_read_local()`: Consume as much local buffer as possible.
