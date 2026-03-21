INSERT INTO product (product_category_id, name, description, price, available_stock)
SELECT pc.product_category_id, np.name, np.description, np.price, 0
FROM new_product np
JOIN product_category pc ON pc.name = np.product_category_name;

SELECT * FROM product ORDER BY product_id DESC;
