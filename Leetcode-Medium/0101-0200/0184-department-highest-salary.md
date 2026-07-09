# 0184. Department Highest Salary

## Mysql

```mysql
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(salary) 
    FROM Employee 
    WHERE departmentId = e.departmentId
);
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT 
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM (
    SELECT *,
           RANK() OVER (PARTITION BY departmentId ORDER BY salary DESC) AS rnk
    FROM Employee
) e
JOIN Department d ON e.departmentId = d.id
WHERE e.rnk = 1;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT d.name   AS Department,
       e.name   AS Employee,
       e.salary AS Salary
FROM ( SELECT e.*,
              DENSE_RANK() OVER (PARTITION BY e.departmentId ORDER BY e.salary DESC) AS rnk
       FROM Employee e ) e
JOIN Department d ON e.departmentId = d.id
WHERE e.rnk = 1;
```

## Pythondata

```pythondata
import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    merged = employee.merge(department, left_on='departmentId', right_on='id')
    merged = merged.rename(columns={'name_x': 'Employee',
                                    'salary': 'Salary',
                                    'name_y': 'Department'})
    max_salary = merged.groupby('Department')['Salary'].transform('max')
    result = merged[merged['Salary'] == max_salary][['Department', 'Employee', 'Salary']]
    return result
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT d.name AS Department,
       e.name AS Employee,
       e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE e.salary = (
    SELECT MAX(salary)
    FROM Employee
    WHERE departmentId = e.departmentId
);
```
