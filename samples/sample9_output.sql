-- Output: Databricks SQL case sensitivity
SELECT employee_id, name
FROM employees
WHERE name ILIKE 'JOHN';
