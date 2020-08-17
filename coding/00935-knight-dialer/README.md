# Knight Dialer

https://leetcode.com/problems/knight-dialer/

## Solution

It's a regular DFS. We need to create a table of the next step for searching.

```
_NEXT = (
    (4, 6),    # 0
    (6, 8),  # 1
    (7, 9),  # 2
    (4, 8),  # 3
    (0, 3, 9),  # 4
    None,    # 5
    (0, 1, 7),  # 6
    (2, 6),  # 7
    (1, 3),  # 8
    (2, 4),  # 9
)
```

Notice that 5 can jump to nowhere. The tricky thing is that, if the knight is placed on 5 already, and we have no more
steps to move, we should return 1. Otherwise, we should return 0.

The rest is a regular DFS.
