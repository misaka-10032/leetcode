# The Skyline Problem

[Origin](https://briangordon.github.io/2014/08/the-skyline-problem.html).

* Critical point: top left or top right of a rectangle.
 * `c.x`: x axis of critical point
 * `c.y`: y axis (height) of critical point
 * `c.left`: t/f marking if it's the left side of rectangle.
* For all critical points, find all rectangle who is taller.
 * Update `c.y` to be `h` of the tallest rectangle covering it.
* Scan over the sorted critical points.
 * Maintain a max heap of them: push at left; pop at right.
 * Peak the top of heap to get `h` of the tallest rectangle covering it.
 * As python only has min heap, we can use `-c.y` as key.
 * As heap doesn't support popping arbitrary node, use a set to record popped nodes.
 * Every time before peaking at the heap, pop (both from heap and set) until top is not in set.
* Finally we need to compress the list by deleting `c` with the same `h`.

## Improvements

* Don't need to pop the rectangle at the right edge.
 * Maintain not only `-rect.y`, but also `rect.right`.
 * When the current `c` sees `top.right < c.x`, keep popping it.

It seems `dict` and object with fields is slow in python, though complexity is `O(1)`.
The faster code is not as readable as the previous ones.
