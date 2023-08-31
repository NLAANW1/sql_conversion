-- databrics output from oracle window functions
SELECT employee_id, salary, 
       RANK() OVER (ORDER BY salary DESC) as rank
FROM employees;
