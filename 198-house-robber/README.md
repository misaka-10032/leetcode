# House Robber

* Let `f[i]` be max amount we can grab in `[0, i)`
* `f[i]` will be max of
  * `f[i-1]`
  * `f[i-2]+a[i-1]`
* Init
  * `f[-1] = f[0] = 0`

### Optimization

* Only previous two are needed: `f[i-1]` and `f[i-2]`
