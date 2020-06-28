# Maximum Product of Word Lengths

* Hash word to integer, so that each bit represent a letter.
* A valid pair `(a, b)` would have `a & b == 0`.
* Pre-hash to reduce complexity.
* Use list rather than dict to store hashed values.