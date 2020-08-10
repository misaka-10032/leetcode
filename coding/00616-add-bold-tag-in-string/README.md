# Add Bold Tag in String

https://leetcode.com/problems/add-bold-tag-in-string/

## Solution

The first step is to build an array of bool that indicates if a char is bold or not. The second step is to add bold
tags at the boundaries (0 to 1 or 1 to 0 or the very beginning or the very end).

The dictionary can be arranged into a Trie tree for efficiency. Whenever we find a word in the Trie tree, we set the
bold bits accordingly.
  