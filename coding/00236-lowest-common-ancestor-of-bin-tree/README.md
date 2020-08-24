# Lowest Common Ancestor of a Binary Tree

## Two Pass Solution

* Keep track of parents of nodes by iterating the tree.
* Generate a path to root for `p` and `q`.
* Go reversely and find the last equal element.
* e.g.
  * `p->r` may look like `[4, 2, 5, 3]`
  * `q->r` may look like `[5, 3]`
  * Go reversely through two list and find `5` is the last equal element,
    which is LCA.

## One Pass Solution

* Iterate the tree once.
* Each node tells whether it has `p` or `q`.
* If it both then return itself as LCA and pass it on.
