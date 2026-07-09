# 1517. Find Users With Valid E-Mails

## Mysql

```mysql
SELECT user_id, name, mail
FROM Users
WHERE mail REGEXP '^[A-Za-z0-9][A-Za-z0-9._-]*@leetcode\\.com$';
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT user_id, name, mail
FROM Users
WHERE LEFT(mail, 1) <> '.'
  AND (LEN(mail) - LEN(REPLACE(mail, '@', ''))) = 1
  AND SUBSTRING(mail, CHARINDEX('@', mail) + 1, LEN(mail)) = 'leetcode.com'
  AND mail NOT LIKE '%[^a-zA-Z0-9._-]%';
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT user_id,
       name,
       mail
FROM   Users
WHERE  REGEXP_LIKE(mail, '^[A-Za-z0-9][A-Za-z0-9._-]*@leetcode\.com$');
```

## Pythondata

```pythondata
import pandas as pd

def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    pattern = r'^[A-Za-z0-9][A-Za-z0-9._-]*@leetcode\.com$'
    mask = users['mail'].str.contains(pattern, regex=True, na=False)
    return users[mask]
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT user_id, name, mail
FROM Users
WHERE mail ~ '^[A-Za-z0-9][A-Za-z0-9._-]*@leetcode\.com$';
```
