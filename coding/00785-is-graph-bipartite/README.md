# Is Graph Bipartite?

https://leetcode.com/problems/is-graph-bipartite/

## Solution

We traverse the graph and add the nodes to `S` set or `T` set intermittently. We start with `S` set, and stop when the
next node exists already in `S` set or `T` set. If existence is contradictory to our current expectation, we should
return `False`.
 