# Best Time to Buy and Sell Stock

* The problem can be formalized into

$$
\begin{align*}
\max_{i, j} &\quad c_j - c_i \\
\text{s.t.} &\quad i \le j
\end{align*}
$$

* Let `f[j]` be max profit if we sold at day `j`.
* `f[j] = c[j] - min(c[:j+1])`
* `min` can be maintained when scanning.
* Max profit can also be maintained during scanning.
* $O(n)$ time and $O(1)$ space.
