# Wildcard Matching

FSA exceeds time limit, as dfs consumes exponential time. Greedy will do for this problem.

Example 1

```
a b c d e f g h
a ? c *     g h
```

Example 2

```
a b c x x d e f g h
a ? c *   d e f g h
```

* Normal character and `?` are one-to-one match
* `*` can choose to match or not match
* Try match `*` first, if mismatch happens, try ignore it and start over again.
* Contiguous `*` should be ignored
* Don't early terminate because `p` goes to end, only do with `s`.
