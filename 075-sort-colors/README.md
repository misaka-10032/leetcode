# Sort Colors

### Dutch national flag problem

* Maintain three pointers `i`, `j`, `k`, such that
  * `[0, i)` are for `0`s.
  * `[i, j)` are for `1`s.
  * `[k, n)` are for `2`s.
* When `j` and `k` meets, sorting completes.
