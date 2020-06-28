# Remove Duplicate Letters

* Make lazy decisions.
* For example

```
0, 1, 2, 3, 4, 5, 6, 7, 8, 9
b, d, c, d, f, e, c, d, a, f
```

* First, find the last appearance for each letter

```
a: 8
b: 0
c: 6
d: 7
e: 5
f: 9
```

* Sort according to last appearance

```
(0, b), (5, e), (6, c), (7, d), (8, a), (9, f)
```

* Make decisions according to this order
* Every decision maker at least yields itself;
  it may also yield those before it if that is smaller.

### Example

* When `(0, b)` makes decision, it looks back and find it's the only one, so

```
['b']
```

* When `(5, e)` makes decision, it looks back and sees `d, c, d, f, e`.
  It yields those `<=` itself, iteratively. Proceeds with a `start` pointer,
  so that it never looks back those before `start`. __Repeat until `e` is yielded.__
  The decision for this iteration is

```
['c', 'd', 'e']
```

* When `(6, c)` makes decision, it finds that `c` is already yielded, so skip it.
* So as to `(7, d)`
* When `(8, a)` makes decision, it looks back and only finds itself, so it yields

```
['a']
```

* When `(9, f)` makes decision, it looks back and only finds itself, so it yields

```
['f']
```

* Concatenate all the decisions, and get the result.

```
['b'] + ['c', 'd', 'e'] + ['a'] + ['f']
```
