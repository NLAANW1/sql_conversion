-- Complex SQL Query 2
WITH ranked_orders AS (
  SELECT order_id, product_id, order_date,
         ROW_NUMBER() OVER (PARTITION BY product_id ORDER BY order_date) AS rank
  FROM order_details
)
SELECT product_id, COUNT(DISTINCT order_id) AS distinct_orders
FROM ranked_orders
WHERE rank = 1
GROUP BY product_id
HAVING distinct_orders >= 10
