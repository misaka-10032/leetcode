# Reverse Nodes in k-Group

* Reverse the first group in case there's no `k` elements.
* Extract the routine of reversing inside the group.
* Reverse group by group; be careful of those on the edge.
* For a group identified by `left` and `right`, we also need to track `pre_left` and `post_right` to hook up the change.