# Meeting Rooms

## Description 

* Given an array of meeting time intervals consisting of
  start and end times `[[s1,e1],[s2,e2],...] (si < ei)`.
  Determine if a person could attend all meetings.

* For example,
  * Given `[[0, 30],[5, 10],[15, 20]]`,
  * return false. 

## Solution

* Sort according to starting time.
* Only need to compare this starting time and previous end time.
