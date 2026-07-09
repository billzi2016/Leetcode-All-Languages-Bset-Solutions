# 1050. Actors and Directors Who Cooperated At Least Three Times

## Mysql

```mysql
SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT
    actor_id,
    director_id
FROM
    ActorDirector
GROUP BY
    actor_id,
    director_id
HAVING
    COUNT(*) >= 3;
```

## Oraclesql

```oraclesql
SELECT actor_id,
       director_id
FROM   ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(*) >= 3;
```

## Pythondata

```pythondata
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    cnt = (
        actor_director
        .groupby(['actor_id', 'director_id'])
        .size()
        .reset_index(name='cnt')
    )
    result = cnt[cnt['cnt'] >= 3][['actor_id', 'director_id']]
    return result.reset_index(drop=True)
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT
    actor_id,
    director_id
FROM
    ActorDirector
GROUP BY
    actor_id,
    director_id
HAVING
    COUNT(*) >= 3;
```
