# Spiral Matrix

* Do a spin at a time.
* Spin is defined by
  * Starting location
  * Width
  * Height
* Initially append the first element.
* Then spin.
  * The next would be `w-2` and `h-2`.
* Stop when width is 0 or height is 0.
* Last batch needs to be processed.
  * If `w == 0`, there could be a col left.
  * Elif `h == 0`, there could be a row left.
