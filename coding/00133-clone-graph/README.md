# Clone Graph

* Need to keep track of `old2new`, which records the mapping
  from old node to new node.
* Because, old node can find link to old node, we need a way
  to link new node to the other new node when copying the link.
