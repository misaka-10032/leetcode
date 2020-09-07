# Next Greater Element I

https://leetcode.com/problems/next-greater-element-i/

## Solution

For efficient lookup, we need to build a dict mapping the value to its next greater element. To build the dict, we can
scan the array, and rely on a stack to track the past element. We keep the element decreasing in the stack. Whenever we
see a new element, we try to pop as many smaller elements as possible from the stack, and build the map before popping.
After that, we push the new element to the stack. Here is an example.

```
5,3,4,...
    ^
```

When we see 5, we push it to the stack, because the stack is empty. When we see 3, we push it to the stack, because 5 is
bigger. When we see 4, we connect 3 to 4, and pop 3. We stop popping because 5 is greater. Then we push 4 to the stack,
and continue scanning. 

Once we build the map, we can scan the input array, and answer the queries efficiently.
