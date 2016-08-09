# Trapping Rain Water

[Description](https://leetcode.com/problems/trapping-rain-water/)

* Use a stack to keep track of indices of bars.
* Each time a new bar comes, pop the previous bars and compute the water in that level.

pop

```
                  __
               __|
   __         |
  |  |__......|
  |     |_____|
  |    j        i
```

pop

```
                  __
               __|
   __.........|
  |  |__......|
  |     :.....:
  | j           i
```

push

```
                  __
               __|
              :
              :
              :
                   i
```

* Stack is necessary, as it helps get rid of middle hills.

```
__                           __
  |             __             |      __
  |       __   |               |__   |
  |_...._|  |__|      ==>      :  |__|

   compress
```

* Specifically, the contiguous stages of the same length will be compressed into one. 

```
 ____             __
|    |     =>    |  |
```
