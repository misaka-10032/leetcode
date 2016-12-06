# Meeting Rooms II

## Description

* Given an array of meeting time intervals consisting of start and end times 
  `[[s1,e1],[s2,e2],...]`, find the minimum number of conference rooms required..
* e.g. given `[[0, 30],[5, 10],[15, 20]]`; return `2`.

## Solution - map only

* Well, heap is kind of waste full.
* Actually we only maintain a map `time` to `cnt`
  * `+1` at starting point
  * `-1` at end point
* Then iterate the map according to sorted `time` order,
  and update the `max_cnt` in the meanwhile.

## Solution - heap

### Idea

* Only edges of intervals matters.
* The current right edge only cares how many right edges are after it,
  while these right edges have already pushed.
* Push/pop rule depends on the values,
  so maintain a heap.

### Implementation

* Data structures
  * `l2r` maps left edges to right edges.
  * `heap` is min heap of right edges.
* First, generate edges, and sort them according to position.
* Iterate the edges,
  * If it's left, push it's right edge.
  * If it's right, ...
* When it's right,
  * keep popping until the heap top is greater than
    or equal to its value.
