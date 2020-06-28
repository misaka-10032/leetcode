# Paint Fence

## Description

* Given a fence with `n` posts. Paint it with `k` colors.
* No more than 2 adjacent fence posts should have the same color.

## Solution dp 2

* States can be compressed
* You don't care what exact color is this color and the previous one;
  you only care about if they are different
* `f[i][*]`
  * Painting the `i`th fence
  * `f[i][0]` denotes `this != prev` in color.
  * `f[i][1]` denotes `this == prev` in color.
* Transition
  * `f[i][0] = (f[i-1][0]+f[i-1][1]) * (k-1)`
  * `f[i][1] = f[i-1][0]`
* Init
  * `f[1][0] = k*(k-1)`
  * `f[1][1] = k`
  * Start from `i=2`
* Edge
  * `n=0`: return 0.
  * `n=1`: return k.
* `i` can be compressed, as `f[i][:]` only depends on `f[i-1][:]`

## Solution dp 1

* `f[i][k1][k2]`
  * Painting the `i`th fence
  * Paint the current fence as color `k1`
  * The previous one was painted color `k2`
  * How many choice do I have up till this state?
* Transition
  * Depends on `f[i-1][k2][k3]`
  * Discuss `k2 == k3` or not
* Init
  * `f[1][k1][k2] = 1`
  * Start from `f[2][:][:]`
* Edge
  * `n = 0`
  * `n = 1`
