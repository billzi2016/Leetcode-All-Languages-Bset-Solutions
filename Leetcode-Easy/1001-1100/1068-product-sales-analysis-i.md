# 1068. Product Sales Analysis I

## Mysql

```mysql
SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p ON s.product_id = p.product_id;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT
    p.product_name,
    s.year,
    s.price
FROM
    Sales AS s
JOIN
    Product AS p
ON
    s.product_id = p.product_id;
```

## Oraclesql

```oraclesql
SELECT p.product_name,
       s.year,
       s.price
FROM   Sales s
JOIN   Product p
ON     s.product_id = p.product_id;
```

## Pythondata

```pythondata
import pandas as pd

def sales_analysis(sales: pd.DataFrame, product: pd.DataFrame) -> pd.DataFrame:
    merged = sales.merge(product, on="product_id", how="inner")
    return merged[["product_name", "year", "price"]]
```

## Postgresql

```postgresql
SELECT p.product_name, s.year, s.price
FROM Sales s
JOIN Product p ON s.product_id = p.product_id;
```
