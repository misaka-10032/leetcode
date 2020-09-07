# Word Ladder

https://leetcode.com/problems/word-ladder/

## Solution

First, let's add `beginWord` to `wordList` and build a graph given the words. Two words should be connected iff they
have a single char being different. There are two ways to build the graph. One way is to iterate the words and compare
them char by char. The other way is to iterate the words, change one char, and see if the new word appears in the dict.
If we denote the length of the dict as `n`, and the word length as `m`, then the first approach has complexity
`O(n*n*m)`, and the second approach has complexity `O(n*m*26*m)`. The first approach is preferred if the dict is long;
the second approach is preferred if the word is long.

Given the graph, we can do a bi-directional BFS. We start with two dicts: `s_depths` and `t_depths`, and two queues:
`s_queue` and `t_queue`. We keep probing in one set, swapping, and probing in the other set, until we touch the other
set.
