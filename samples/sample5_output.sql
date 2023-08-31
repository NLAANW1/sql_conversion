-- Databricks SQL leverages Spark's partitioning especially when reading from distributed file systems
CREATE TABLE employees_partitioned (employee_id INT, department_id INT, salary INT)
USING DELTA
PARTITIONED BY (salary);
