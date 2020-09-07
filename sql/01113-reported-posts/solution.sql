# Write your MySQL query statement below
SELECT
  extra as report_reason,
  count(distinct(post_id)) as report_count
FROM Actions
WHERE
  action = 'report' AND
  action_date = '2019-07-04'
GROUP BY report_reason

