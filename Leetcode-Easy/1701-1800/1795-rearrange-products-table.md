# 1795. Rearrange Products Table

## Mysql

```mysql
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products
WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products
WHERE store3 IS NOT NULL;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2', store2
FROM Products
WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3', store3
FROM Products
WHERE store3 IS NOT NULL;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT product_id,
       'store1' AS store,
       store1   AS price
FROM   Products
WHERE  store1 IS NOT NULL
UNION ALL
SELECT product_id,
       'store2' AS store,
       store2   AS price
FROM   Products
WHERE  store2 IS NOT NULL
UNION ALL
SELECT product_id,
       'store3' AS store,
       store3   AS price
FROM   Products
WHERE  store3 IS NOT NULL;
```

## Pythondata

```pythondata
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    result = products.melt(id_vars=["product_id"], var_name="store", value_name="price")
    return result.dropna(subset=["price"]).reset_index(drop=True)
```

## Postgresql

```postgresql
SELECT product_id, 'store1' AS store, store1 AS price
FROM Products
WHERE store1 IS NOT NULL
UNION ALL
SELECT product_id, 'store2' AS store, store2 AS price
FROM Products
WHERE store2 IS NOT NULL
UNION ALL
SELECT product_id, 'store3' AS store, store3 AS price
FROM Products
WHERE store3 IS NOT NULL;
```
