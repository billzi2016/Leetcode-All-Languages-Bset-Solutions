# 0178. Rank Scores

## Mysql

```mysql
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores
ORDER BY score DESC;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;
```

## Pythondata

```pythondata
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    df = scores.copy()
    df["rank"] = df["score"].rank(method="dense", ascending=False).astype(int)
    result = df.sort_values(by="score", ascending=False)[["score", "rank"]]
    return result.reset_index(drop=True)
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT
    score,
    DENSE_RANK() OVER (ORDER BY score DESC) AS rank
FROM Scores
ORDER BY score DESC;
```
