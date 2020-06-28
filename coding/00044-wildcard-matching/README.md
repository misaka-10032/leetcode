# Wildcard Matching

## KMP

* Greedy has worst time complexity of `O(n^2)`
* KMP can achieve complexity of `O(m+n)`
* Idea is to split `p` by `*`

### KMP table

```
  failure jump
    |-----|
a b c a b d
  j     i
```

* `j` and `i` points to the __last match__.

## Greedy

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

### Things to remember

* Master pointer on `s`. Pointer on `p` moves accordingly.
* Proceed and regret.
* Let `s_reg` be `i+1`.
* Let `p_reg` be `j`.
* Allow `*`s at the end of `p`.
