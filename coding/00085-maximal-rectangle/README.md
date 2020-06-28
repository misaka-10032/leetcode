# 85. Maximal Rectangle

* Each cell picks as much as possible upwards, and finds its left/right boundaries

```
    1 1
  1 1 1 1
1 1 1 1 1 1
```

* Height

```
    1 1
  1 2 2 1
1 2 3 3 2 1
```

```
if matrix[i][j] == '1':
    height[i][j] = height[i-1][j] + 1
else:
    height[i][j] = 0
```

* Left (inclusive)

```
    2 2
  1 2 2 1
0 1 2 2 1 0
```

```
if matrix[i][j] == '1':
    left[i][j] = max(leftmost, left[i-1][j])
else:
    left[i][j] = 0; leftmost = j+1
```

* Right (exclusive)

```
    4 4
  5 4 4 5
6 5 4 4 5 6
```

```
if matrix[i][j] == '1':
    right[i][j] = min(rightmost, right[i-1][j])
else:
    right[i][j] = n; rightmost = j
```

* Tricky: Only one row of storage of `height`, `left`, `right` is needed
  * For each `left`, we only need max of `leftmost` from the current row and the previous one.
  * For each `right`, we only need min of `rightmost` from the current row and the previous one.
