SELECT
  Score,
  (SELECT COUNT(*)
   FROM (SELECT DISTINCT Score s FROM Scores) AS UniScores
   WHERE s >= Score)
  AS Rank
FROM
  Scores
ORDER BY Score DESC;