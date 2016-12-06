SELECT w1.Id
FROM
  Weather w1,
  Weather w2
WHERE
  w1.Temperature > w2.Temperature AND
  TO_DAYS(w1.Date) - TO_DAYS(w2.Date) = 1;
