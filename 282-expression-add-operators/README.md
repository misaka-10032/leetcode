# Expression Add Operators

### Solution

* The only bad guy is `*`
* We eval while proceeding, but need to keep track of
  `regret` variable, which, if the upcoming is `*`, we
  can regret the previously added value, and update with
  the new value.

### Naive

* Add operator before current position.
* `eval` result at last
* No consecutive `0`s: `00` is invalid.
* Slow
* Refactor to memorized `dfs`
  * get rid of global tracking of `curr` and `res`
  * Encode the result in return value
* Still slow, because `eval` is slow.
