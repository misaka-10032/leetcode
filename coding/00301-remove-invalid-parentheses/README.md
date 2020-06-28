# Remove Invalid Parentheses

## Wrong solution

* Divide the string into unbalanced groups.
* Two types of unbalance
  * Type I `())`: left < right
  * Type II `(()`: left > right
* The groups will be like multiple type I's followed by one or none type II.
* Generate balanced list for groups.
* Counter example

```
)()))())))
  ^^^
```

* The marked three right parentheses can all be removed without pairing up with the first `(`.

## Correct solution

* Define `ub=left-right`
* The system only allows `ub>=0`
* Once `ub==-1`, the system begin to clean up possible `)`s.

### Unbalanced right

```
()))...(...
 ^^
```

* The first two rights are must-remove ones.
* The third one is optional in case that `(` appears later.

### Unbalanced left

```
...)...((()
       ^^
```

* If it turns out to have more `(`s than `)`s,
  we may go reversely and do exactly the same again.

### Implementation Trick

* Two passes
  * Forward pass removes extra `)`s.
  * Backward pass removes extra `(`s.
  * After these two stages, add the string to result list.
* Constrain only remove from the leftmost `)`s.
  * e.g. `((())..`, if we decide to preserve the first `)`,
    the second `)` should also be preserved.
* Two pointers
  * `front` probes the valid boundary on the right.
  * `rear` points to the leftmost eligible `)`.
