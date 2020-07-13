# Alien Dictionary

* You receive a list of words from the dictionary,
  where words are sorted lexicographically by the rules of this new language.

```
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]
```

* One possible result would be `wertf`.

## Solution

* Find dependencies by comparing neighboring words
* There're two ways to do topological sort
  * Iterative approach: Kahn's algorithm
  * DFS: compare in/out time
* O(|V| + |E|)

### Kahn's alg

* This simple solution uses the same idea, but
  a little different from the standard data structure,
  so it has a little higher complexity.
* Nodes are chars
* Dependency is described with a str like `ab`,
  meaning `a -> b`.
* Data structures
  * `heads`: set of nodes with no in-coming links.
  * `deps`: the current dependencies. Keep updating this
    after removing some `heads`.
  * `remain`: set of uncleared nodes (chars)
  * `order`: list of sorted chars
* Python tricks
  * zip: `zip([a1, a2], [b1, b2])` becomes `[(a1, b1), (a2, b2)]`.
  * unzip: `zip(*[(a1, b1), (a2, b2)])` converts it back.
* The solution is neat, but the worst case can be slow, e.g.
  * `a -> b -> c -> d -> ...`
  * The complexity could be `O(n^2)`

### DFS

* maintain `t_in` and `t_out`
* append in out-order, and finally reverse it
* Checking non-back edge (u -> v) by checking if
  * `t_in_u < t_in_v < t_out_v < t_out_u` or
  * `(t_in_v < ) t_out_v < t_in_u ( < t_out_u)`
