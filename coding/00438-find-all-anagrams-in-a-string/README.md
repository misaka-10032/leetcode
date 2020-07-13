# Find All Anagrams in a String

https://leetcode.com/problems/find-all-anagrams-in-a-string/

## Solution

The anagram can be matched by matching the counters of the chars. Assuming `s` has `n` chars and `p` has `m` chars,
there will be `n-m+1` windows to match, and each window could take `O(m)`, so the naive solution would take `O(mn)`.

Instead of directly matching the counters, we can maintain a "residual" counter map, which tracks how many more chars
are needed to reach the target `p`. The matching becomes `O(1)` because we only need to check if the map is empty.

Before we start, the counters contain all the chars in `p`.

```
 cbaeb
^abc
```

When we move the pointer, we start to cancel chars by decrementing the counter. We also increment the counter for the
char at the left boundary. 

```
 cbaeb
 ^ab
```

When the map becomes empty, we append the index to the global result.

```
 cbaeb
   ^
 012
 ^
```

When we see an unseen char, we count it as -1.

```
 cbaeb
    ^c(-e)
```

We remove an element from the map when the counter goes from 1 to 0 or from -1 to 0.
