# Q2 — SQL INSERT from temp table (Question 2/5)

Retail shop database. Import new products from a temporary table into the main product table.

## Schema

**product_category**: product_category_id (PK), name VARCHAR(50), description VARCHAR(255)

**product**: product_id (PK), product_category_id (FK), name VARCHAR(50), description VARCHAR(255), price DECIMAL(5,2), available_stock INTEGER

**customer**: customer_id (PK), firstname, lastname, birth_date, address, zipcode, city, phone_number

**purchase_order**: order_id (PK), customer_id (FK), date

**order_product**: order_id (FK), product_id (FK) — junction table

## Task

`new_product` (temp table) has fields: `product_category_name`, `name`, `description`, `price`

Insert into `product` such that:
- `name`, `description`, `price` — transferred directly
- `product_id` — auto-set
- `available_stock` — set to 0
- `product_category_id` — resolved by matching `new_product.product_category_name` to `product_category.name`

Guaranteed: every `new_product.product_category_name` matches an existing `product_category.name`.

`product` table: 21 rows → 45 rows after insert.

## Validation query (do not modify)

```sql
SELECT * FROM product ORDER BY product_id DESC;
```
