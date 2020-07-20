# Binary Search Tree Iterator

## Generator

* [Generator Tutorial](https://wiki.python.org/moin/Generators)
* [Generator with both return and yield](http://stackoverflow.com/a/26595922/3663161)
* `dfs` and change `return` to `yield`
* Take what is yielded as a list and use `for ... in dfs(...)`.

## Stack

* In-order traversal with stack.
* Initially push all the left descendants of `root` onto stack.
* Whenever goes to a node (with `next`), push all the left
  descendants of right subtree onto stack.
 