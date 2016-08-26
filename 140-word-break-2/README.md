# Word Break II

* Represent `curr` as list of words in `dict`.
* The state includes the start pointer `k`.

### Pruning

* Some patten can appear multiple times, cache it
  * e.g. `'abab ababab'`
* Kind of like cheating, taking a lot of space.
