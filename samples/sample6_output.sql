-- handeling null values
-- Output: Databricks SQL
SELECT COALESCE(salary, 0) AS adjusted_salary
FROM employees
WHERE job_id IS NULL;
