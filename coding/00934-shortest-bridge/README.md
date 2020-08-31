# Shortest Bridge

https://leetcode.com/problems/shortest-bridge/

## Solution

The problem guarantees there are two islands, so it makes the problem easier. We first DFS the graph to find the two
islands. Then, we pick the smaller island, and keep growing it until it touches the other island. The growing step is
BFS. We can mark the grown part to island (`1`) to prevent growing twice on the same point.
