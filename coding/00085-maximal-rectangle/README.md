# 85. Maximal Rectangle

https://leetcode.com/problems/maximal-rectangle/

## Solution

The idea is to fix the iterated element at the bottom of a rectangle, and then find its top, left, right boundaries. We
can track the boundaries in a very tricky way when we iterate the matrix.

### Top Boundary

The top boundary is the first `0` above. Thus, we can simply track an array of `top` indices for each column. For
example,

```
Row 0: 1  0  0  0  1  0
Row 1: 1  1  1  0  1  0
Row 2: 1  1  0  0  1  0  <- current row
...

Top:  -1  0  2  2 -1  2
```

To put it as code, we have the following.

```
top = [-1] * n
for i in range(m):
  for j in range(n):
    top[j] = top[j] if matrix[i][j] == '1' else i
```

### Left / Right Boundary

The left / right boundary is symmetric, so I will only discuss the left boundary. It is more tricky than the top
boundary. It requires the columns till the boundary to have at least the same (or higher) top boundaries. For example,

```
Col:     0  1  2  3  4  5

Row 0:   1  0  0  0  1  0
Row 1:   1  1  1  0  1  0
Row 2:   1  1  0  0  1  0  <- previous row
Row 3:   1  0  1  1  1  1  <- current row
...

Left 2: -1 -1 -1 -1  3 -1  <- previous row
Left 3: -1 -1  1  1  3  1  <- current row
```

The `left` array depends on two arguments. The first is the current row; the second is the `left` array of the previous
row. For the current row, the first zero on the left can possibly shorten the left bound.  For the previous row, the
previously shortened left bound cannot be increased, i.e.

```
new_left = max(prev_left, new_left)
```

We have a tricky update rule for `0`: we need to reset the left boundary to `-1`, because the following rows can go to
the very left, and no column can have a lower top than the current column. To put it as code, we have the following.

```
left = [-1] * n
for i in range(m):
  leftmost = -1
  for j in range(n):
    if matrix[i][j] == '1':
      left[j] = max(left[j], leftmost)
    else:
      left[j] = -1
      leftmost = j
```

### Compute the Area

```
area = (i - top[j]) * (right[j] - left[j] - 1)
```

### Complexity

`O(m*n)`.

## Alternative Solution

Instead of fixing the point to be on the base, we can also make it at the top-left corner. However, we have to probe the
right boundaries for all the following rows. The probing can be `O(1)` once we precomputed the first `0` on the right.
However, the row probing cannot be saved. In total, we have `O(m*n)` elements, and each element has `O(m)` rows to
probe. To pre-compute the first `0` on the right, we need `O(m*n)`. Therefore, the total time complexity is `O(m*m*n)`.
We can possibly transpose the matrix to save some computation.
