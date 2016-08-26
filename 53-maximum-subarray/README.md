# Maximum Subarray

* If `curr_sum` is still `> 0`, continue on this cohort.
* Keep updating `best` in the meanwhile.
* If `curr_sum` begins to `< 0`, begin with next cohort.
* Edge case: `nums` has all `< 0`, pick the max.
