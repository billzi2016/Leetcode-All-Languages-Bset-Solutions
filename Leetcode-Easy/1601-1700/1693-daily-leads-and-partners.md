# 1693. Daily Leads and Partners

## Mysql

```mysql
SELECT date_id,
       make_name,
       COUNT(DISTINCT lead_id)   AS unique_leads,
       COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT 
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY 
    date_id,
    make_name;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id)   AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY date_id, make_name;
```

## Pythondata

```pythondata
import pandas as pd

def daily_leads_and_partners(daily_sales: pd.DataFrame) -> pd.DataFrame:
    return (
        daily_sales
        .groupby(['date_id', 'make_name'], as_index=False)
        .agg(unique_leads=('lead_id', 'nunique'),
             unique_partners=('partner_id', 'nunique'))
    )
```

## Postgresql

```postgresql
SELECT
    date_id,
    make_name,
    COUNT(DISTINCT lead_id) AS unique_leads,
    COUNT(DISTINCT partner_id) AS unique_partners
FROM DailySales
GROUP BY
    date_id,
    make_name;
```
