# 2356. Number of Unique Subjects Taught by Each Teacher

## Mysql

```mysql
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```

## Oraclesql

```oraclesql
SELECT teacher_id,
       COUNT(DISTINCT subject_id) AS cnt
FROM   Teacher
GROUP  BY teacher_id;
```

## Pythondata

```pythondata
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    return (
        teacher.groupby("teacher_id")["subject_id"]
        .nunique()
        .reset_index(name="cnt")
    )
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT
    teacher_id,
    COUNT(DISTINCT subject_id) AS cnt
FROM Teacher
GROUP BY teacher_id;
```
