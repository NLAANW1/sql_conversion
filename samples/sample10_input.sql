-- Input: Oracle SQL limiting rows
SELECT employee_id, name
FROM employees
WHERE ROWNUM <= 10;
