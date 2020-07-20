# Add and Search Word

* Trie

```
            root
      /  /  |  |  \  \ ...      
     a  b   c  d  ...
   node(is_word)
/  |  |  \ ...
a  b  c  ...
   | 
node(is_word)
```

* Dfs for `.`
* It's important to have an `is_word` field to track whether the word appears. Otherwise, the fact that a node appears
  only indicates the substring so far appears.
  * For example, `abc` is add, and then we query `ab`. There will be a node for `ab`. We need `is_word` to tell if the
    the word `ab` is added before.