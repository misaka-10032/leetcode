# Minimum Knight Moves

https://leetcode.com/problems/minimum-knight-moves/

## Solution

First, let's find the boundary of the search space. We could possibly jump back 2 spaces to borrow a space in the other
direction, but we won't jump back more in the optimal solution. Therefore, the search space is restricted in
```
xmin, xmax = min(0, x) - 2, max(0, x) + 2
ymin, ymax = max(0, y) - 2, max(0, y) + 2
```

Second, as we want to find a shortest path in a comparatively open space, we should do BFS. To search more efficiently,
we should do **bidirectional** BFS. We put a night at both the starting point and the target point, and probe in both
directions. The probed area from the starting point will be added to an `s` map, and the probed area from the target
point will be added to a `t` map. The map tracks the mapping from the position to the number of hops. When a hop from
`s` reaches `t` or vice versa, a solution is found. The nature of BFS guarantees the path is the shortest.
 