# Wiggle Subsequence

* Toggle between `should_small` and `!should_small`.
* When it's correct, move on.
* When it's wrong, try to regret
  * If previous is `should_small` and it's smaller, then replace it.
  * If previous is `!should_small` and it's larger, then replace it.
