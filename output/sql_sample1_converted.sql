-- Converted Databricks SQL from sql_sample1.sql
-- 
-- Complex SQL Query 1
SELECT customer_name, COUNT(*) AS order_count
FROM orders
INNER JOIN customers ON orders.customer_id = customers.id
WHERE orders.order_date >= '2023-01-01'
GROUP BY customer_name
HAVING order_count > 5
