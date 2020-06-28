# Ugly Number II

* Each new number will step on the previous number.
* Each factor (`2`, `3`, `5`) will only step on a previous number once.
  * e.g. once `2` stepped on `6` and becomes `12`, it will never
    step on `6` again.
  * Next time `2` may step on `8`, the next ugly number of `6`,
    and will never skip `8` and step on `9`, the next ugly number of `8`.
* Keep track of the level that factors (`2`, `3`, `5`) have climbed.
* Compare and determine whose turn it is to generate the next ugly number.
* Be careful it's possible that a new ugly can be generated in different ways.
  * e.g. `6`
  * That `2` climbs from `3` (_3_rd ugly) makes a `6`.
  * That `3` climbs from `2` (_2_nd ugly) also makes a `6`.
