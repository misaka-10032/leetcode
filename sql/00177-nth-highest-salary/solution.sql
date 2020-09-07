/*
[LIMIT {[offset,] row_count | row_count OFFSET offset}]
 */

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE i INT;
  SET i = N-1;
  RETURN (

    SELECT DISTINCT Salary FROM Employee
    ORDER BY Salary DESC
    LIMIT 1 OFFSET i

  );
END