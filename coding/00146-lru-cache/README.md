# LRU Cache

* `dict` maps from `key` to `node`
* `node`s form a doubly linked list

```
lru <-> ... <-> mru
```

* Be careful of several edge cases
 * What if node is `lru`
 * What if node is `mru`
 * What if `cap` is zero
