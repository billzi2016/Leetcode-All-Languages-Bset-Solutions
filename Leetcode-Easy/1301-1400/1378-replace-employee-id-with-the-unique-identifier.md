# 1378. Replace Employee ID With The Unique Identifier

## Mysql

```mysql
SELECT u.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS u ON e.id = u.id;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT u.unique_id, e.name
FROM Employees AS e
LEFT JOIN EmployeeUNI AS u
    ON e.id = u.id;
```

## Oraclesql

```oraclesql
SELECT
    u.unique_id,
    e.name
FROM Employees e
LEFT JOIN EmployeeUNI u ON e.id = u.id;
```

## Pythondata

```pythondata
import pandas as pd

def replace_employee_id(employees: pd.DataFrame, employee_uni: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(employees, employee_uni, how='left', on='id')
    return merged[['unique_id', 'name']]
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT u.unique_id,
       e.name
FROM   Employees e
LEFT JOIN EmployeeUNI u
       ON e.id = u.id;
```
