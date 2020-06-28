# Find Duplicate Number

* [Reference](http://keithschwarz.com/interesting/code/?dir=find-duplicate)
* Let `f` be mapping from index to value.
  * e.g. `[1, 2, 3, 4]`
  * `f(0) = 1`, `f(1) = 2`, ...
  * `D(f) = [0, n+1)`
  * `R(f) = [1, n+1)`
* __Claim 1__: If there's duplicate, there's cycle.
* __Proof 1__: Reduce to contradiction. If there's no cycle, the `[0, n+1)`
  will produce `n+1` different numbers within `[1, n]`, which is impossible!
* __Claim 2__: The duplicate is the entry of the cycle.
* __Proof 2__: Let's say `f[i] = f[j] = k`. The chain looks like

```
           ↙ j ...
... → i → k → ...
```

`k` is the only node which has $d_{in}>1$. All the other nodes have $d_{in}=d_{out}=1$.
Such node is exactly the entry of a cycle.
