### Jump Game II

* DP exceeds time limit; use BFS
* Element in the deque is the index of which we've arrived.
* Need also maintain a `dist` array to avoid pushing index twice, as we know the first arrived has shortest distance.