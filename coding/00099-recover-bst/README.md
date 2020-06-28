# Recover BST

* In-order traversal of BST is an ordered list, e.g.

```
[0, 1, 2, 3, 4, 5]
```

* If two elements are switched, we can recover them by comparing
with the previous node.

```
[0, 5, 2, 3, 4, 1]
 t, t, f, t, t, f
     \          |
      first   second
```

* After finding `first` and `second`, we can simply switch them.

# Morris Traversal

[Example](http://stackoverflow.com/questions/5502916/explain-morris-inorder-tree-traversal-without-using-stacks-or-recursion)
[Blog](http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html)

```
* Init current as root
* Maintain prev and curr
* While current is not None
  * If current doesn't have left subtree
    * Print current
    * Go to right
  * Elif current has left subtree
    * Make current (and its right subtree) the rightmost node of its left subtree
    * If the rightmost doesn't have right
      * Thread the right of rightmost to current 
      * Go to left
    * Else the rightmost has been threaded to current already
      * Clean up the thread
      * Go to right
  
```

## Detailed illustration

* If current does NOT have left subtree

```
  a (curr)                    a
   \                           \
    b     -->  print a  -->     b (curr)
   / \                         / \
 ... ... 
```

* If rightmost of the left subtree has not yet been threaded

```
    a (curr)                           a    - - - - - - - - -+
   / \                                / \                    :
  b                           (curr) b                       :
 / \                                  \                      :
    c                                  c                     :
     \                -->             / \                    :
     ...                                ...                 ...
       \                                  \                  :
        d (rightmost)                      d (rightmost) - - +
       /                                  /
```

* `curr` will turn around and finally go back to `a`

```
   a    - - - - +                    a (curr)  - - - - +
  /             :                   /                  :
 b              :                  b                   :
  \             :                   \                  :
   c (curr)     :                    c                 :
  / \           :   -->  ...  -->   / \                :
    ...        ...                    ...             ...
      \         :                       \              :
       d  - - - +                        d   - - - - - +
      /                                 /
```

* Then it will find the rightmost of the left subtree has already been threaded,
because right of `rightmost` points to `curr` it self. Then simply remove the thread.

```
    a (curr)  - - - - - - +                            a
   / \                    :                           / \
  b                       :                          b   (curr)
 / \                      :                         / \
    c                     :                            c
     \                    :    -->  print a  -->        \
     ...                 ...                            ...
       \                  :                               \
        d (rightmost) - - +                                d
       /                                                  /
```
