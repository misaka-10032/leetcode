# Write your MySQL query statement below

WITH
  UniqueSpamPosts AS (
    SELECT
      DISTINCT(post_id),
      1 AS counter,
      action_date
    FROM Actions
    WHERE
      extra = 'spam'
  ),
  RemovedPosts AS (
   SELECT
     DISTINCT(post_id),
     1 AS counter
   FROM Removals
  ),
  DailyPercent AS (
    SELECT
      COALESCE(SUM(RP.counter), 0) / SUM(USP.counter) AS daily_percent
    FROM
      UniqueSpamPosts USP LEFT JOIN RemovedPosts RP ON
        USP.post_id = RP.post_id
    GROUP BY action_date
  )
SELECT
  ROUND(AVG(daily_percent) * 100, 2)
    AS average_daily_percent
FROM DailyPercent

