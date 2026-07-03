# 0175. Combine Two Tables

## Mysql

```mysql
SELECT p.FirstName, p.LastName, a.City, a.State
FROM Person AS p
LEFT JOIN Address AS a ON p.PersonId = a.PersonId;
```

## Mssql

```mssql
SELECT p.FirstName,
       p.LastName,
       a.City,
       a.State
FROM Person AS p
LEFT JOIN Address AS a
    ON p.PersonId = a.PersonId;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT p.FirstName,
       p.LastName,
       a.City,
       a.State
FROM   Person p
LEFT JOIN Address a
ON     p.PersonId = a.PersonId;
```

## Pythondata

```pythondata
import pandas as pd

def combine_two_tables(person: pd.DataFrame, address: pd.DataFrame) -> pd.DataFrame:
    merged = pd.merge(person, address, on="personId", how="left")
    return merged[["firstName", "lastName", "city", "state"]]
```

## Postgresql

```postgresql
SELECT p.firstName, p.lastName, a.city, a.state
FROM Person AS p
LEFT JOIN Address AS a ON p.personId = a.personId;
```
