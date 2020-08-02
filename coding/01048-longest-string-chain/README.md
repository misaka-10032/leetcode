# Longest String Chain

https://leetcode.com/problems/longest-string-chain/

## Solution

We save all the words in a set, and search the longest chain that ends with the current word. In addition, we maintain a
cache of the length of the searched chain, so we don't search twice.

### Complexity

Let's say we have `k` words, and the longest word has `m` chars. As we cached result for each word, we only need to go
though the actual search of the predecessor once for each word. The predecessor search costs `O(m)`, and we have `k`
words in total, so we have `O(k*m)` time complexity in total.

The space is reserved for the word set and the cache result. They both cost `O(k*m)` in space.
