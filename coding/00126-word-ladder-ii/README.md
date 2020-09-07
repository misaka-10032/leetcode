# Word Ladder II

https://leetcode.com/problems/word-ladder-ii/

## Solution

It's similar to [the previous problem](https://leetcode.com/problems/word-ladder/), except that we no longer care about
the depth, but care about the word list.

```
@dataclasses.dataclass
class BfsState:
    graph_node: Node
    word_list: List[str]
```

In addition, we don't early return if we reach the same frontier with a different path. To achieve this, we don't probe
one step at a time; we probe the entire frontier. We allow different paths to the frontier, but won't allow revisiting
the points within the frontier.

### Alternative

BFS stores exponentially more intermediate state than DFS. To save space, we can only use BFS to find the shortest path,
and use DFS to back trace the combinations.
