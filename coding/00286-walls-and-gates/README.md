# Walls and Gates

* INF(2147483647) means room
* -1 means wall
* 0 means gates

```
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
```

* Modify in-place, so that the result is the
  distance to the closest gate.

## Solution

* DFS
* Keep track of visited.
* State: (i, j, d)
* Push `0` cells to queue.
* Only visit the `INF` cells.
