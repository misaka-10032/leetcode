# Shortest Distance from All Buildings

https://leetcode.com/problems/shortest-distance-from-all-buildings/

## Solution

Build a map of distances (`dists[i][j]`) from all the buildings (`1`) to the empty lands (`0` at `(i, j)`). We iterate
the buildings, and do a BFS to compute the distances for that building. The distance can be simply added to the global
`dists` array.

There is one minor optimization to save the search space. If some empty land cannot be reached by a certain building, we
can mark it as an obstacle (`2`). 

For BFS, we generally prefer to set a point visited before pushing it to the queue, because we can save time and space
for multiple equal-length paths to the same point

```
  -------> path1
 | +---+
 | |   |
 | +---+  target
 v path2
```
