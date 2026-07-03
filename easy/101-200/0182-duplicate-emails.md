# 0182. Duplicate Emails

## Mysql

```mysql
SELECT
    email AS Email
FROM
    Person
GROUP BY
    email
HAVING
    COUNT(*) > 1;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```

## Pythondata

```pythondata
import pandas as pd

def duplicate_emails(person: pd.DataFrame) -> pd.DataFrame:
    duplicated = person['email'][person['email'].duplicated(keep=False)].unique()
    return pd.DataFrame({'Email': duplicated})
```

## Postgresql

```postgresql
SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(*) > 1;
```
