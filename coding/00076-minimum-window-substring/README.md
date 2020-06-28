# Minimum Window Substring

* Two pointers `i`, `j` defines the current window `[i, j)`.
* Move `j` forward until there's no missing.
* Move `i` forward as much as possible.
* Maintain a counter `need`, which counts how many chars are still required.
  * e.g. `{'A': 2}` means 2 more `A`s are required to make a match.
  * `{`a`: -2}` means we have 2 more `a`s than required.
  * Only update those in `need` (in `t`)!
* `missing` can be maintained while proceeding.
  * Only when `need` item is `>0`, `missing` decreases.
  * It does not increase, as after first match, we will never make it unmatched again.
