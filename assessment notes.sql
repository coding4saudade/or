
-- order_history: order-level information, including customer id, order total and date
-- order_line: per-product information for an order
-- product: product information
-- product_price_history - product pricing.



-- We’d like to see a summary of units sold per product. For each product, display the product id and name combined, calling this field product_desc. Along with that product description, display the total units of that product that have been ordered.





Challenge 1
select concat(p.product_id,
p.product_name) AS product_desc,
sum(product_qty) AS total_units
FROM product AS p 
INNER JOIN order_line AS o 
  ON p.product_id = o.product_id
GROUP BY product_desc;




-- Challenge 2
-- How long has it been since customers have ordered a product? For all products that have been ordered, display the product id, product name, and the most recent order date.

Select DISTINCT p.product_id,
p.product_name,
o.order_date 


FROM order_history AS o
INNER JOIN order_line AS ol 
  ON o.order_id = ol.order_id
INNER JOIN product AS p 
  ON ol.product_id = p.product_id

PARTITION BY p.product_id


-- GROUP BY p.product_id, p.product_name, o.order_date
-- ORDER BY o.order_date DESC;




-- Challenge 3
-- On average, what are customers paying for each product? For all products that have been ordered, display the product id, product name, and average per-unit price that customers have paid for that product.