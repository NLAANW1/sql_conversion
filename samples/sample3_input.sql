-- Oracle Hierarchical queries 
SELECT employee_id, manager_id
FROM employees
START WITH manager_id IS NULL
CONNECT BY PRIOR employee_id = manager_id;
