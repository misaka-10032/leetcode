# Word Break II

* Represent `curr` as list of words in `dict`.
* The state includes the start pointer `k`.

### Cache

* Some patten can appear multiple times, cache it
  * e.g. `'abab ababab'`
* `cache[k]` is a `list` of all combinations of `s[k:]`.
* `s[k:k+l] in dict ? cache[k].extend(map(..., f[k+l]))`

### Memorized dfs vs dp

* dfs could terminate early

```
a...a b a..a
```

* culprit `b` would have dfs terminate early, but
  dp would keep trying the suffixes.
