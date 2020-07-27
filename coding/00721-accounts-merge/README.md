# Accounts Merge

https://leetcode.com/problems/accounts-merge/

## Solution -- DFS

If a user has multiple emails, we add a **bidirectional** edge between the first email and the additional emails. We
iterate the unvisited emails, use them as seeds, and explore the connected components. The connected components consist
of all the emails owned by a user.

We also need to track the mappings from email to name, because the final result needs them.

## Solution -- Union Find Set

A [union-find set](https://en.wikipedia.org/wiki/Disjoint-set_data_structure) is a set-like data structure that allows
efficient connectivity queries. It supports the following operations:

* `add(key)`: Add a key to the set.
* `find(key)`: Find the representative of the component that the key belongs to.
* `union(key1, key2)`: Joins the two components that `key1` and `key2` belong to respectively. A new representative will
  be elected if `key1` and `key2` belongs to two different components.

The data structure consists of two maps.

* `parents`: Maps a key to its parent key. Following the map we can find the representative of the component.
* `ranks`: Tracks the ranks of the **root** keys. It is a proxy of the depth of the tree (it can change later during
  `find()` queries). This `rank` provides guidance in how to elect a new representative during `union()`: putting the
  low-rank tree under a high-rank tree produces a shorter tree, and therefore is more friendly for `find()` queries.

Given this data structure, we keep merging the additional emails of the same user with the first email. In another pass,
we iterate all the emails, and put them under the root email.

## Solution -- Flat Union Find Set

As the result asks for all the emails of the same component, we can make a slight change in the union-find set by
tracking all the children instead of parents. This can help us save the extra pass of grouping. During merging, we
should put the smaller component under the bigger one for efficiency.
 