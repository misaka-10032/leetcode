# Patching array

* Strategy is patch the farthest reach to fully make use of the numbers at hand.
* For example

```
1, 3, 100 
```

* Init with range `[0, 1)`.
* When we see `1`, it's about the farthest reach, so simply update the range to `[0, 2)`.
* Then we see `3`, it's out of the current reach, so we patch the farthest reach `2`.
  Now the range becomes `[0, 4)`.
* `3` is now within reach, so update the range to `[0, 7)`
* `100` is out of reach, so patch the farthest reach `7`, and update range to `[0, 14)`
  * Still out of reach, patch `14`; update range to `[0, 28)`
  * Still out of reach, patch `28`; update range to `[0, 56)`
  * ...