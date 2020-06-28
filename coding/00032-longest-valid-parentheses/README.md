# Longest Valid Parentheses

Keep track of index with stack. Consider this two cases

```
()(()
```

vs

```
(()()
```

* Push the index of unmatched `(` or `)` to stack.
* Matched `(` will be popped.
* Finally those between stack elements are matched up chunks.
* We only need to find the max len of chunks
separated by these unmached `(` or `)`:

__)(__ ()() __((__ (())...
