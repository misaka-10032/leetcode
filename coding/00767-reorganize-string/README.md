# Reorganize String

https://leetcode.com/problems/reorganize-string/

## Solution

According to the [pigeonhole principle](https://en.wikipedia.org/wiki/Pigeonhole_principle), there will not be solution
if the most frequent char appears more than `(n+1)//2` times.

Otherwise, we can interleave the most frequent element, and fill in other elements in-between. If the most frequent
element does not span the entire array, we can continue to use the second, the third, etc., and it does not matter.

We sort the chars by their inverse frequency. We pick the first half `(n+1)//2` and span the array after every other
element.

```
result[::2] = sorted_chars[:mid]
```

We then pick the second half, and stuff the rest.

```
result[1::2] = sorted_chars[mid:]
```

The elements that are not most frequent are guaranteed to be surrounded by elements that are not themselves, because
they are less frequent than the most frequent elements that are already spanned.
