# Similar String Groups

https://leetcode.com/problems/similar-string-groups/

## Solution

Build a graph that connects the similar words. Traverse the graph to count the connected components.


There are two ways to build the graph. One way is to iterate all the word pairs. The other way is to iterate
the word and then iterate all the possible similar words, and see if they exist in the word set.

To analyze the complexity, let's denote the list length is `n` and the word length is `m`. The first approach would
cost `O(n*n)` in word-pair iteration, and `O(m)` in comparison, so in total, it's `O(n*n*m)`.

The second approach would cost `O(n)` in word iteration, `O(m*m)` in neighbor iteration, and `O(m)` in neighbor
creation, so in total `O(n*m*m*m)`.

We should build the graph in the first approach if `n*n*m < n*m*m*m`, and otherwise in the second approach.
