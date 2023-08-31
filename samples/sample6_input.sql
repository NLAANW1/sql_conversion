-- handling nulls
-- Input: Oracle SQL
SELECT NVL(salary, 0) AS adjusted_salary
FROM employees
WHERE job_id IS NULL;

