# Course Schedule III

https://leetcode.com/problems/course-schedule-iii/

## Solution

First, we sort the courses by their end time. Then we iterate the sorted courses, and try to add them to the schedule.
If we miss the deadline, we will try to replace a course with longer duration. To do this, we can find the course with
longest duration in the past. If we are able to make the time by replacing this course, we replace it. Otherwise, we do
nothing.

To find a course with the max duration, we can use a heap. Essentially, we only need to track the durations of all the
scheduled courses, and return the heap size in the end.
