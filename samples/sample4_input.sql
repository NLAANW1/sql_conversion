-- oracle window functions
WITH recursive_cte AS (
  SELECT employee_id, manager_id
  FROM employees
  WHERE manager_id IS NULL
  UNION ALL
  SELECT e.employee_id, e.manager_id
  FROM employees e
  JOIN recursive_cte r ON e.manager_id = r.employee_id
)
SELECT * FROM recursive_cte;
