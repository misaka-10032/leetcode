# Number of Islands II

## Description

* Begin with empty map with size `m, n`
* Plant islands on the map, given positions

```
[[0,0], [0,1], [1,2], [2,1]]
```

* Return number of islands at every moment.

```
1, 1, 2, 3
```

## Solution

* Union find set: map from node to root.
* In this problem, grid is dense, so 2d-array is ok
  (don't have to be dict).
* Each time, look up the 4 neighbors and see if there's any connection.
* Path compression: pick the most `cnt` as root

## Debug

* Didn't append `tot` in early `continue`.
* Subtract one more from `tot` even for the master root itself.
* Picked the least `cnt`, omg...
  * Change from least to most: 14% to 68% in leetcode.
