# 1729. Find Followers Count

## Mysql

```mysql
SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT 
    user_id,
    COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT user_id,
       COUNT(*) AS followers_count
FROM   Followers
GROUP BY user_id
ORDER BY user_id;
```

## Pythondata

```pythondata
import pandas as pd

def count_followers(followers: pd.DataFrame) -> pd.DataFrame:
    result = (
        followers
        .groupby('user_id', as_index=False)
        .size()
        .rename(columns={'size': 'followers_count'})
        .sort_values('user_id')
        .reset_index(drop=True)
    )
    return result
```

## Postgresql

```postgresql
SELECT user_id, COUNT(*) AS followers_count
FROM Followers
GROUP BY user_id
ORDER BY user_id;
```
