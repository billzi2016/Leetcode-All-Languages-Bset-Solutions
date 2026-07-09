# 3497. Analyze Subscription Conversion

## Mysql

```mysql
SELECT 
    user_id,
    ROUND(AVG(CASE WHEN activity_type = 'free_trial' THEN activity_duration END), 2) AS trial_avg_duration,
    ROUND(AVG(CASE WHEN activity_type = 'paid' THEN activity_duration END), 2) AS paid_avg_duration
FROM UserActivity
WHERE activity_type IN ('free_trial', 'paid')
GROUP BY user_id
HAVING COUNT(CASE WHEN activity_type = 'paid' THEN 1 END) > 0
ORDER BY user_id;
```

## Mssql

```mssql
/* Write your T‑SQL query statement below */
SELECT
    user_id,
    CAST(ROUND(AVG(CASE WHEN activity_type = 'free_trial' THEN activity_duration END), 2) AS DECIMAL(10,2)) AS trial_avg_duration,
    CAST(ROUND(AVG(CASE WHEN activity_type = 'paid'       THEN activity_duration END), 2) AS DECIMAL(10,2)) AS paid_avg_duration
FROM UserActivity
GROUP BY user_id
HAVING SUM(CASE WHEN activity_type = 'paid' THEN 1 ELSE 0 END) > 0
ORDER BY user_id;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT user_id,
       ROUND(AVG(CASE WHEN activity_type = 'free_trial' THEN activity_duration END), 2) AS trial_avg_duration,
       ROUND(AVG(CASE WHEN activity_type = 'paid' THEN activity_duration END), 2) AS paid_avg_duration
FROM UserActivity
WHERE activity_type IN ('free_trial', 'paid')
GROUP BY user_id
HAVING COUNT(CASE WHEN activity_type = 'paid' THEN 1 END) > 0
ORDER BY user_id;
```

## Pythondata

```pythondata
import pandas as pd

def analyze_subscription_conversion(user_activity: pd.DataFrame) -> pd.DataFrame:
    trial = (
        user_activity[user_activity["activity_type"] == "free_trial"]
        .groupby("user_id", as_index=False)["activity_duration"]
        .mean()
        .rename(columns={"activity_duration": "trial_avg_duration"})
    )
    paid = (
        user_activity[user_activity["activity_type"] == "paid"]
        .groupby("user_id", as_index=False)["activity_duration"]
        .mean()
        .rename(columns={"activity_duration": "paid_avg_duration"})
    )
    result = pd.merge(trial, paid, on="user_id")
    result["trial_avg_duration"] = result["trial_avg_duration"].round(2)
    result["paid_avg_duration"] = result["paid_avg_duration"].round(2)
    result.sort_values("user_id", inplace=True)
    return result
```

## Postgresql

```postgresql
-- Write your PostgreSQL query statement below
SELECT
    user_id,
    ROUND(AVG(CASE WHEN activity_type = 'free_trial' THEN activity_duration END)::numeric, 2) AS trial_avg_duration,
    ROUND(AVG(CASE WHEN activity_type = 'paid' THEN activity_duration END)::numeric, 2) AS paid_avg_duration
FROM UserActivity
WHERE activity_type IN ('free_trial', 'paid')
GROUP BY user_id
HAVING SUM(CASE WHEN activity_type = 'paid' THEN 1 ELSE 0 END) > 0
ORDER BY user_id;
```
