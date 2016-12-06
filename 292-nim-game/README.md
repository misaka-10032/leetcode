# Nim Game

## Description

You are playing the following Nim Game with your friend:
There is a heap of stones on the table, each time one of you 
take turns to remove 1 to 3 stones. The one who removes the 
last stone will be the winner. You will take the first turn to 
remove the stones.

Both of you are very clever and have optimal strategies for the game.
Write a function to determine whether you can win the game given 
the number of stones in the heap.

For example, if there are 4 stones in the heap, 
then you will never win the game: no matter 1, 2, or 3 stones 
you remove, the last stone will always be removed by your friend.

## Solution

* Will only lose at 4, 8, 12, ...

## Naive solution

* N position: I win.
* P position: The previous play wins.
* Denote
  * 0 as P position
  * 1 as N position
  * `f[k]` as P/N position given k nimbers
* `f[k] = not f[k-1] or not f[k-2] or not f[k-3]`
* Actually it only depends on the previous 3 states, so
  it can be compressed.
