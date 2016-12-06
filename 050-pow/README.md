* `n` could be positive and negative
  * >=0 then start with `x`
  * < 0 then start with `1./x`
* Maintain
  * `level` as level product
  * `tot` as total product
* move on with `n >>= 1`
