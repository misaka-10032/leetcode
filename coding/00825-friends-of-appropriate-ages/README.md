# Friends Of Appropriate Ages

https://leetcode.com/problems/friends-of-appropriate-ages/

## Solution

Group the people by age, and iterate the group pairs. For people from different age groups, the follow count should be
multiplied by `cnt1 * cnt2`. For people from the same age group, the follow count should be multiplied by
`cnt * (cnt - 1)`, because people cannot follow themselves.
