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

* Left (inclusive)

```
    2 2
  1 2 2 1
0 1 2 2 1 0
```

* Right (exclusive)

```
    4 4
  5 4 4 5
6 5 4 4 5 6
```

* Tricky: Only one row of storage of `height`, `left`, `right` is needed
  * For each `left`, we only need max of `leftmost` from the current row and the previous one.
  * For each `right`, we only need min of `rightmost` from the current row and the previous one.
