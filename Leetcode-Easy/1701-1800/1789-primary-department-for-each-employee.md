# 1789. Primary Department for Each Employee

## Mysql

```mysql
# Write your MySQL query statement below
SELECT employee_id, department_id
FROM (
    SELECT *, COUNT(*) OVER (PARTITION BY employee_id) AS cnt
    FROM Employee
) e
WHERE cnt = 1 OR primary_flag = 'Y';
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT employee_id, department_id
FROM (
    SELECT *, COUNT(*) OVER (PARTITION BY employee_id) AS emp_cnt
    FROM Employee
) AS e
WHERE emp_cnt = 1 OR primary_flag = 'Y';
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT employee_id,
       department_id
FROM (
    SELECT e.*,
           COUNT(*) OVER (PARTITION BY employee_id) AS emp_cnt
    FROM Employee e
)
WHERE emp_cnt = 1 OR primary_flag = 'Y';
```

## Pythondata

```pythondata
import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    employee_counts = employee.groupby('employee_id')['employee_id'].transform('size')
    return employee[(employee_counts == 1) | (employee['primary_flag'] == 'Y')][['employee_id', 'department_id']]
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT employee_id,
       department_id
FROM (
    SELECT *,
           COUNT(*) OVER (PARTITION BY employee_id) AS emp_cnt
    FROM Employee
) AS sub
WHERE emp_cnt = 1 OR primary_flag = 'Y';
```
