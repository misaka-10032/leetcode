# Best Time to Buy and Sell Stock III

* Let `fwd[i]` be the greatest profit if sold before or at `i`th day.
* Let `bwd[i]` be the greatest profit if bough after or at `i`th day.
* Bellman equation
  * `fwd[i] = max(fwd[i-1], c[i]-min(c[:i+1]))`
  * `bwd[i] = max(bwd[i+1], max(c[i:])-c[i])`
  * `best = max_i(fwd[i] + bwd[i])`
