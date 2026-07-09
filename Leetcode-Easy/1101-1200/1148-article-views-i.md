# 1148. Article Views I

## Mysql

```mysql
# Write your MySQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
```

## Pythondata

```pythondata
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    result = (
        views[views["author_id"] == views["viewer_id"]]
        ["author_id"]
        .drop_duplicates()
        .sort_values()
        .reset_index(drop=True)
        .to_frame(name="id")
    )
    return result
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT DISTINCT author_id AS id
FROM Views
WHERE author_id = viewer_id
ORDER BY id;
```
