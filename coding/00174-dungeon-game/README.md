# Dungeon Game

### Wrong strategy

* Here's a common mistake that we may make
* Let `f[i][j]` be min health required to reach `(i, j)`
* Let `g[i][j]` be the actual health remained when we pick the optimal
  path to `(i, j)`
* If top is picked, health at `(i, j)` would become `h_actual = g[i-1][j] + a[i][j]`
  * If the actual health `h_actual>0`, everything's good: 
    `h_min = f[i-1][j]`.
  * If the actual health becomes `t<=0`,
    `h_min = f[i-1][j]-t+1` and `h_actual = 1`.
* Similar analysis applies to left.
* Now compare which strategy is better:
  * The strategy with smaller `h_min` is picked.
  * If `h_min` are the same, then the one with larger `h_actual` is picked.
* It's wrong as it's possible we abandon a power-up because of the other path requires
  minimum health. However, we don't know what happens in the future. It's possible that
  the future cell has a great amount of threat, and the cell we abandoned previously may
  just be enough to balance that threat. Therefore, the strategy is sub-optimal.

### Correct strategy

* Think reversely. The best strategy must have the knight as less health left as possible.
* Denote `f[i][j]` as __lower bound__ of actual health remained at cell `(i, j)`
  __before__ taking power-up or damage.
* `f[i][j] = max(1, min(f[i+1][j], f[i][j+1]) - a[i][j])`;
  `1` is a lower bound for the lower bound.
* Edge case
  * `f[i][n-1] = max(1, f[i+1][n-1]-a[i][j])`
  * `f[m-1][j] = max(1, f[m-1][j+1]-a[i][j])`
* Init `f[m-1][n-1] = max(1, 1-a[i][j])`
