-- oracle partationing sample 
CREATE TABLE employees_partitioned (
  employee_id NUMBER,
  department_id NUMBER,
  salary NUMBER
) PARTITION BY RANGE (salary) (
  PARTITION p1 VALUES LESS THAN (5000),
  PARTITION p2 VALUES LESS THAN (10000),
  PARTITION p3 VALUES LESS THAN (MAXVALUE)
);
