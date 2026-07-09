# 1327. List the Products Ordered in a Period

## Mysql

```mysql
SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT p.product_name,
       SUM(o.unit) AS unit
FROM Orders o
JOIN Products p ON o.product_id = p.product_id
WHERE o.order_date BETWEEN '2020-02-01' AND '2020-02-29'
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT p.product_name,
       SUM(o.unit) AS unit
FROM   Products p
JOIN   Orders o ON p.product_id = o.product_id
WHERE  o.order_date BETWEEN DATE '2020-02-01' AND DATE '2020-02-29'
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;
```

## Pythondata

```pythondata
import pandas as pd

def list_products(products: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Ensure order_date is datetime
    if orders['order_date'].dtype != 'datetime64[ns]':
        orders = orders.copy()
        orders['order_date'] = pd.to_datetime(orders['order_date'])
    
    # Filter for February 2020
    feb_orders = orders[
        (orders['order_date'].dt.year == 2020) &
        (orders['order_date'].dt.month == 2)
    ]
    
    # Sum units per product
    agg = feb_orders.groupby('product_id', as_index=False)['unit'].sum()
    
    # Keep products with at least 100 units
    qualified = agg[agg['unit'] >= 100]
    
    # Join with product names
    result = qualified.merge(
        products[['product_id', 'product_name']],
        on='product_id',
        how='inner'
    )
    
    return result[['product_name', 'unit']]
```

## Postgresql

```postgresql
SELECT p.product_name, SUM(o.unit) AS unit
FROM Products p
JOIN Orders o ON p.product_id = o.product_id
WHERE o.order_date BETWEEN DATE '2020-02-01' AND DATE '2020-02-29'
GROUP BY p.product_name
HAVING SUM(o.unit) >= 100;
```
