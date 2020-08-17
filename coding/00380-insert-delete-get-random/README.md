# Insert Delete GetRandom O(1)

https://leetcode.com/problems/insert-delete-getrandom-o1/

## Solution

A `dict` can do `insert` and `remove` in constant time, but cannot do random access. A `list` can do random access, but
cannot do constant-time `insert` and `remove`. The solution is to maintain both data structures and benefit from both.

* `vals`: a `list` of all values.
* `v2i`: a `dict` mapping values to indices.

The tricky thing is about `remove`. If we leave a hole in the array, it makes the further random access difficult.
However, we can swap the element with the last element before removing it. 
