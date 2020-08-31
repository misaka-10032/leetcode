# Making A Large Island

https://leetcode.com/problems/making-a-large-island/

## Solution

First, DFS the graph to find the connected islands. We need to give the island an index, and count its size. Thus, the
first function should give us two arrays: `island_ids` and `island_sizes`. `island_ids` has the same size as `grid`, and
`island_sizes` has length being the number of islands.

Then, we iterate the water to find the unique islands it touches. The contribution of this water is the sum of the size
of the unique islands plus one (from this water).

There are two corner cases to address: 1) if all the regions are water, 2) if all the regions are lands. The first case
should return 1, and the second case should return the map size.
