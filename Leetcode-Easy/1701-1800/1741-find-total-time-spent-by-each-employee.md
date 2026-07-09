# 1741. Find Total Time Spent by Each Employee

## Mysql

```mysql
SELECT 
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;
```

## Oraclesql

```oraclesql
SELECT event_day AS day,
       emp_id,
       SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;
```

## Pythondata

```pythondata
import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    df = employees.copy()
    df["total"] = df["out_time"] - df["in_time"]
    result = (
        df.groupby(["event_day", "emp_id"], as_index=False)["total"]
        .sum()
        .rename(columns={"event_day": "day", "total": "total_time"})
    )
    return result[["day", "emp_id", "total_time"]]
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT 
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY event_day, emp_id;
```
