# Word Break

https://leetcode.com/problems/word-break/

## Solution

We can introduce a recursive function `_search(i)` to return whether `s[i:]` consists of the words in `wordDict`.

The same `i` might be passed in multiple times if the first time fails. To save the useless search to come, we can use
an array `doomed` to track whether `s[i:]` cannot be decomposed properly. We don't need to track whether we can, because
whenever we find a possible decomposition, we will quickly return and get out of the recursion.

### Complexity

Let's denote the length of `s` is `m`, the length of the word dict is `n`, and the average length of word in the word
dict is `l`. The worst case is that we search all the words at all the chars at `s`. We only search them once due to the
optimization from `doomed`. Therefore, the time complexity will be `O(m*n*l)`.

If the dictionary happens to be too large, we have two possible optimizations: 1) build a Trie from the dict, and track
the trie node during search. 2) Build a set from the dict, and compute the shortest / longest word length. Each time, we
only search for a valid length range, and check if the word is in the dict. 
