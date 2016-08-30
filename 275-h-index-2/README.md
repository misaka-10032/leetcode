# H-Index II

* If sorted reversely, find the first index such that `i <= c`.

```
5, 5, 3, 3, 3, 1, 1
0, 1, 2, 3, 4, 4, 5
         ^
```

* If sorted, find the last index such that `n-1-i >= c` 

```
1, 1, 3, 3, 3, 5, 5
0, 1, 2, 3, 4, 5, 6
6, 5, 4, 3, 2, 1, 0
         ^
         p
```

* Suppose final position is `p`, then
  * `a[i] <= n-1-i`, for `i` in `[0, p]`
  * `a[j] > n-1-j`, for `j` in `(p, n)`
* This may be a little bit hard. Now try to find its next element

```
1, 1, 3, 3, 3, 5, 5
0, 1, 2, 3, 4, 5, 6
6, 5, 4, 3, 2, 1, 0
            ^
            q
```

* For this `q`,
  * `a[i] <= n-1-i`, for `i` in `[0, q)`
  * `a[j] > n-1-i`, for `j` in `[q, n)`

* In binary search, it's important to know the right element to find.
* If we can know the characteristics peculiar to elements within `[0, q)`,
  the problem will be much simplified. (Inclusive and exclusive is important).
* By doing this, we can make `i=m+1` or `j=m` without infinite loop.
* Edge case `[0, 0, 0, 0]`: no citation means no h-index.
