SELECT
  d.Name as Department,
  e.Name as Employee,
  e.Salary as Salary
FROM
  Employee as e JOIN Department as d
  ON e.DepartmentId = d.Id
WHERE
  e.Salary >= ALL (
    SELECT ee.Salary
    FROM Employee ee
    WHERE e.DepartmentId = ee.DepartmentId);