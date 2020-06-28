# Largest Rectangle in Histogram

* Simply scan and reset doesn't work; consider this

```
[1, 2, 3, 2, 2, 3, 2, 1] 
```

* The previous `1`, `2` should still be in stack even after we've dealt with `3`.

## Stack solution

* Idea is to book-keep the left boundaries.
* Tricky part is when and how we update the areas.
* Scan bins over
* If it's increasing, push __index__ into stack, as it's potential left boundary.
* If it's decreasing, those greater top's can no longer be left boundaries,
  so pop until top is smaller. In the meanwhile, update max area.
  * Curr is the rightmost reach from stack tops.
  * Leftmost is tricky; it's one plus next element of stack top.
  * e.g. `2, 6, 3, 4, 3`, curr is last, stack is `2, 3`, leftmost is 6, next of 2.
  * `lb = S[-1]+1`, inclusive left bound
  * `rb = i`, exclusive right bound
* When it's __equal__, pop the previous and push the rightmost one as boundary for the upcoming.

```
[0, 1, 2, 3, 2, 1, 2, 3, 2]
    ^  ~~~~~~~  ^
```

* The second `1` in stack keeps the left boundary of `2` on its right.
* The first `1` is no longer needed when the second `1` comes, because
  those between these two `1`s has already been computed the max areas.
