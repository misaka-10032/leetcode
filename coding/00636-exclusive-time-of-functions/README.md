# Exclusive Time of Functions

https://leetcode.com/problems/exclusive-time-of-functions/

## Solution

First, let's redefine `end` as the start of the next timestamp (i.e. the original `end+1`), so the duration can be
computed as `end - start`. The function calls form a stack. In order to compute the exclusive time, we need to track not
only the start time, but also the wait time.

```
f0:  |____       ____       ___|    |
f1:      |__...__|  |__...__|       |
...                                 |
fn:        |___|      |___|        \|/  stack
```

When we push a function, we not only pushes its start time, but also its wait time.

```
stack.append(Timer(start_time=log_item.ts, wait_time=0))
```

When we pop a function, we update its execution time and its parent's wait time.

```
durations[log_item.func_id] += exclusive_duration
parent_timer.wait_time += duration
```
