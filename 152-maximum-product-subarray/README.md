# Maximum Product Subarray

* An interesting fact about product:
  * Max range product can suddenly jump to min, and vice versa.
  * e.g. `[2, 3, -2, -1]`
  * Up to `3`, max range product is (2*3=) 6, min is 3.
  * When it comes to `-2`, the original max (6) becomes min (6*-2=) -12.
  * When it comes to `-1`, the original min (-12) becomes max (-12*-1=) 12.
* When come up with a new `x`, it can
  * Combine with the previous min range.
  * Combine with the previous max range.
  * Start a new range.
* vs max-sum:
  * max-sum only needs streaming max
  * this requires streaming min and max
