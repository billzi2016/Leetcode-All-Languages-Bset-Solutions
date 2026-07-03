# 0181. Employees Earning More Than Their Managers

## Mysql

```mysql
# Write your MySQL query statement below
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT
    e.name AS Employee
FROM
    Employee e
JOIN
    Employee m ON e.managerId = m.id
WHERE
    e.salary > m.salary;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
```

## Pythondata

```pythondata
import pandas as pd

def find_employees(employee: pd.DataFrame) -> pd.DataFrame:
    mgr = employee.rename(columns={"id": "manager_id", "salary": "manager_salary"})
    merged = pd.merge(
        employee,
        mgr[["manager_id", "manager_salary"]],
        left_on="managerId",
        right_on="manager_id",
        how="inner",
    )
    res = merged[merged["salary"] > merged["manager_salary"]][["name"]]
    return res.rename(columns={"name": "Employee"})
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m ON e.managerId = m.id
WHERE e.salary > m.salary;
```
