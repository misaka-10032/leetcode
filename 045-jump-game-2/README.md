### Jump Game II

* DP exceeds time limit

## BFS

* Element in the deque is the index of which we've arrived.
* Need also maintain a `dist` array to avoid pushing index twice,
  as we know the first arrived has shortest distance.

## Greedy

* Inspect the number of step needed

| idx   | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|-------|---|---|---|---|---|---|---|---|---|
| nums  | 2 | 3 | 1 | 1 | 4 | 2 | 1 | 2 | 2 |
| jumps | 1 | 1 | 1 | 2 | 2 | 3 | 3 | 3 | 3 |

* `jumps` denotes number of the jumps needed to reach there.
* We claim that `jumps` is non-decreasing (proof by contradiction).
* Denote the range with the same `jumps` as a cohort
  * `[0, 2]` is the 1st cohort
  * `[3, 4]` is the 2nd cohort
  * `[5, 8]` is the 3rd cohort
  * $[L_k, R_k]$ is the $k$th cohort
* The end of the next cohort is only affected by the farthest reach from this cohort.
  * Start with cohort `1` at  `[0, 2]`.
  * The end of next cohort `2` is determined by

$$
R_{k+1} = \max_{i\in[L_{k}, R_{k}]} i + x_i
$$

* Keep computing $R_{k+1}$ cohort by cohort.
* If somehow $R_{k+1} = R_{k} \neq n-1$, the cohort doesn't proceed. Then it indicates the last index is not reachable.
