# Unique Paths

* Bellman equation: `f[i][j] = f[i-1][j] + f[i][j-1]`
* Init: `f[0][j] = f[i][0] = 0`
