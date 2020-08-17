# Battleships in a Board

https://leetcode.com/problems/battleships-in-a-board/

## Solution

Iterate the board and only increment the counter at the representatives. The representative is the leftmost or the
topmost 'X'. Therefore, we only need to check the left element and the top element. The 'X' at the top or the left
boundaries is representative as well.
