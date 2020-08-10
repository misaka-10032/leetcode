# Maximal Square

https://leetcode.com/problems/maximal-square/

## Solution.

It is an easier version of [85](https://leetcode.com/problems/maximal-rectangle/). The constraint that `h == w` makes
the problem easier, because the dependency on the sub-problems is less.

Let `f[i][j]` be max width if `a[i][j]` is taken as bottom-right corner. It requires `a[i][j]=='1'`, and depends on
  
* `f[i-1][j-1]`
* `f[i-1][j]`
* `f[i][j-1]`

The smallest of the three is the bottleneck hindering a larger square. The initial setup of the recurrent function is
as follows.

```
f[-1][j] = f[i][-1] = 0
```

As an optimization, we only need to store the current row and the previous row.

### Proof of the limited dependency

For symmetry, let's only visit `f[i-1][j]` and `f[i-1][j-1]`, as `f[i][j-1]` is symmetric to `f[i-1][j]`. For
demonstration purpose, let's define `top[i][j]` as the index of the closest 0 on top of `(i, j)`.

If `top[i-1][j] < top[i-1][j-1]`, we will have the following.

```
f[i][j]-1 <= i-top[i-1][j] <= f[i-1][j]
```

Otherwise, 

```
f[i][j]-1 <= i-top[i-1][j-1] <= f[i-1][j-1]
```

The likewise conclusion can be made for `f[i][j-1]`.
