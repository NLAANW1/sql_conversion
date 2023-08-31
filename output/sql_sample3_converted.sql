-- Converted Databricks SQL from sql_sample3.sql
-- sql
SELECT department_name, AVG(salary) AS avg_salary
FROM employees
INNER JOIN departments ON employees.department_id = departments.id
WHERE employees.hire_date >= '2022-01-01'
GROUP BY department_name
ORDER BY avg_salary DESC
LIMIT 5
