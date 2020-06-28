# Best Time to Buy and Sell Stock IV

* Let `f[i][j]` be max profit by making at most `i` transactions within `j` days.
* `f[i][j]` will be the max of the following
  * `f[i][j-1]`: don't make any transaction in `j-1`th day.
  * `max_{l=0..j-2}{ f[i-1][l]+c[j-1]-c[l] }`: do `i-1` transactions within `l` days,
    and buy the `i`th stock in `l`th day and sell it in `j-1`th day.
* Init
  * `f[0][j] = 0`: no profit can be made if no transaction is done.
  * `f[i][0] = 0`: no profit can be done before within zero days.

### Optimization 1

$$
\begin{align*}
&\quad \max_{l=1}^{j-2}\big\{ f_{i-1, l} + c_{j-1} - c_l \big\}
\\&= c_{j-1} + \max_{l=1}^{j-2}\big\{ f_{i-1, l} - c_l \big\}
\end{align*}
$$

* $\max_{l}\big\{ f_{i-1, l} - c_l \big\}$ won't be needed to be computed within every inner loop of `j`. It carries on with `j`.

### Optimization 2

* `f[i][*]` only depends on `f[i][*]` and `f[i-1][*]`, so only two rows are needed.

### Optimization 3

* When `k>=n/2`, we can make as many as transactions, so it's reduced to
  greedy problem in 122.
