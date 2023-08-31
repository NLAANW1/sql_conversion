-- Input: Oracle SQL temporary tables 
CREATE GLOBAL TEMPORARY TABLE temp_employees (employee_id NUMBER, name VARCHAR2(50))
ON COMMIT DELETE ROWS;
INSERT INTO temp_employees VALUES (1, 'John');
