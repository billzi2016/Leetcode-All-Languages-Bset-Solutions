# 1211. Queries Quality and Percentage

## Mysql

```mysql
SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
```

## Mssql

```mssql
SELECT
    query_name,
    ROUND(AVG(CAST(rating AS float) / position), 2) AS quality,
    ROUND(100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) / COUNT(*), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
```

## Oraclesql

```oraclesql
SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END) * 100.0 / COUNT(*), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
```

## Pythondata

```pythondata
import pandas as pd

def queries_stats(queries: pd.DataFrame) -> pd.DataFrame:
    df = queries.copy()
    df["ratio"] = df["rating"] / df["position"]
    df["is_poor"] = (df["rating"] < 3).astype(int)
    result = (
        df.groupby("query_name")
        .agg(
            quality=("ratio", "mean"),
            poor_query_percentage=("is_poor", lambda x: x.mean() * 100),
        )
        .reset_index()
    )
    result["quality"] = result["quality"].round(2)
    result["poor_query_percentage"] = result["poor_query_percentage"].round(2)
    return result
```

## Postgresql

```postgresql
SELECT
    query_name,
    ROUND(AVG(rating::numeric / position), 2) AS quality,
    ROUND(100.0 * SUM(CASE WHEN rating < 3 THEN 1 ELSE 0 END)::numeric / COUNT(*), 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;
```
