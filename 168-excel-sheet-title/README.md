# Excel Sheet Column Title

* A little bit between 26-base number
* If we take `A` as `0` and `Z` as `25`, then empty is not defined.
  For example, compare `(empty)A` and `AA`. How do you convert the
  26-based `AA` to 10-based number?
* In order that empty is defined, we make `A` to be `1` and `Z` to
  be `26`. However, it's still a 26-based number. Globally it looks
  like `[1, 26]`, locally, we minus one to map it into `[0, 25]`.
