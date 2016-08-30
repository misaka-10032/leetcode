# Kth Largest Element in an Array

* Keep run `partition` until we get the right location.
* Convert kth largest into kth smallest.
* `partition` is like keep swapping `a[i]` and `a[j]`. Here are the tricks.
  * Start with `j--`.
  * Introduce randomness to get rid of the worst case.
* Divide and conquer to find the `k`th.
* Total amortized complexity is $O(n)$.

### Proof

* Let $X_i = 1\{p=i\}$, where $p$ is pivot.
* Then

$$
\begin{align*}
T_i &= T(\max\{i, n-i-1\}) + \Theta(n) \\
T &= \sum_i X_i T_i \\
ET &= \sum_i \frac{1}{n}\big( T(\max\{i, n-i-1\}) + \Theta(n) \big) \\
   &= \frac{2\sum_{k=n/2}^{n}T(k)}{n} + \Theta(n) \\
   &\le cn + \Theta(n) \\
   &= \Theta(n)
\end{align*}
$$

* $\max\{i, n-i-1\}$ is to mimic adversarial behavior, to make
  $k$ appear in the worst side.
* The upper bound $cn$ can be proved by mathematical induction: claim for $n$, prove for $n+1$.