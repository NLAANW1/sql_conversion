-- Input: Oracle SQL case sensitivity
SELECT employee_id, name
FROM employees
WHERE UPPER(name) = 'JOHN';
