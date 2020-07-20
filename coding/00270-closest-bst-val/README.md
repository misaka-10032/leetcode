# Closest Binary Search Tree Value

https://leetcode.com/problems/closest-binary-search-tree-value/

## Solution

The closet node is guaranteed to exist in the binary search path. We should simply track the smallest distance and the
node while we search for the target.

### Proof

If the target is found in the node, then the conclusion is trivial.

If the last node in the search path is smaller than the target, then the possible solution can either be this last
node or its successor. Its successor must be one of its ancestors, or it has no successor at all. In either case, the
closest node does exist in the search path.

If the last node in the search path is greater than the target, then the possible solution can either be this last node
or its predecessor. Its predecessor must be one of its ancestors, or it has no predecessor at all. In either case, the
closest node does exist in the search path.
