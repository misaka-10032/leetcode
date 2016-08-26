# Gas Station

* Denote $\Delta_i = Gas_i - Cost_i$
* Denote $[i]_n = i % n$


### Feasibility

* __Claim:__ if $\sum_i \Delta_i \ge 0$, then there is a solution; otherwise there's not.

### Starting Point

* Now assume it's __feasible__ ($\sum_i \Delta_i \ge 0$).
* __Claim:__ if $k = \arg\min_k \sum_{i=0}^k \Delta_i$, then choosing $[k+1]_n$ as starting point will guarantee feasibility.
* __Proof:__

As $k$ minimizes the $\sum_{i=0}^k \Delta_i$, we have

$$
\sum_{i=k+1}^j \Delta_i \ge 0, \quad j = k+1, ..., n-1
$$

Otherwise we can make $k\leftarrow j$ and obtain a smaller partial sum. On the other hand, as we assumed $\sum_i \Delta_i \ge 0$, we have

$$
\begin{align*}
0&\le\sum_{i=0}^{k} + \sum_{i=k+1}^{n-1}
\\&\le \sum_{i=0}^j + \sum_{i=k+1}^{n-1} 
\\&= \sum_{i=k+1}^{[j+n]_n} \quad\quad \text{where } j \le k
\end{align*}
$$

That is to say, starting from $k+1$, we are able to travel to any $j$ before traveling around.
