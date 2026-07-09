# 1757. Recyclable and Low Fat Products

## Mysql

```mysql
SELECT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND recyclable = 'Y';
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT product_id
FROM Products
WHERE low_fats = 'Y' AND recyclable = 'Y';
```

## Pythondata

```pythondata
import pandas as pd

def find_products(products: pd.DataFrame) -> pd.DataFrame:
    return products[(products["low_fats"] == "Y") & (products["recyclable"] == "Y")][["product_id"]]
```

## Postgresql

```postgresql
SELECT
    product_id
FROM
    Products
WHERE
    low_fats = 'Y' AND recyclable = 'Y';
```
