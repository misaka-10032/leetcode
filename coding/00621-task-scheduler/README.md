# Task Scheduler

## Description

You are given a char array representing tasks CPU need to do. It contains capital letters A to Z where each letter
represents a different task. Tasks could be done without the original order of the array. Each task is done in one unit
of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter
in the array), that is that there must be at least n units of time between any two same tasks.

You need to return the least number of units of times that the CPU will take to finish all the given tasks.

Example 1:

```
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
```

Example 3:

```
Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A
```

## Solution

The strategy is to spread the most frequent task(s), and squeeze in other tasks. Without losing generality,
let's assume A and B are the most frequent tasks. Let's call them "pillar" tasks.

```
    A B _ _ A B _ _ A B _ _ A B 
        |-> idle  |
  s00 <-|         |-> s11
```

The optimal solution would leave as few idle slots as possible, and the result equals

```
task_cnt + idle_cnt
```

The rest of the tasks can be distributed in a round robin manner in the idle slots.

```
s00 s10 s20 s01 s11 s21
```

Because the pillar tasks are the most frequent, we don't need to create new idle slots. Once the idle slots are used up,
we can further squeeze the tasks in

```
s02 s12 s22 s03 ...
```

Therefore, the solution is to 1) find the "pillar" tasks, 2) compute the idle slots, 3) fill up the empty slots.