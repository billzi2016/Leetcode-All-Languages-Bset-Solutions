# 1661. Average Time of Process per Machine

## Mysql

```mysql
# Write your MySQL query statement below
SELECT 
    a.machine_id,
    ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a
JOIN Activity b 
    ON a.machine_id = b.machine_id 
   AND a.process_id = b.process_id
WHERE a.activity_type = 'start' 
  AND b.activity_type = 'end'
GROUP BY a.machine_id;
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT 
    a.machine_id,
    ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a
JOIN Activity b
    ON a.machine_id = b.machine_id
   AND a.process_id = b.process_id
WHERE a.activity_type = 'start'
  AND b.activity_type = 'end'
GROUP BY a.machine_id;
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT a.machine_id,
       ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a
JOIN Activity b
  ON a.machine_id = b.machine_id
 AND a.process_id = b.process_id
WHERE a.activity_type = 'start'
  AND b.activity_type = 'end'
GROUP BY a.machine_id;
```

## Pythondata

```pythondata
import pandas as pd

def get_average_time(activity: pd.DataFrame) -> pd.DataFrame:
    # Separate start and end records
    starts = activity[activity["activity_type"] == "start"]
    ends = activity[activity["activity_type"] == "end"]
    
    # Merge on machine_id and process_id to pair each start with its end
    merged = pd.merge(
        starts,
        ends,
        on=["machine_id", "process_id"],
        suffixes=("_start", "_end")
    )
    
    # Compute processing time for each process
    merged["proc_time"] = merged["timestamp_end"] - merged["timestamp_start"]
    
    # Average per machine and round to 3 decimal places
    result = (
        merged.groupby("machine_id")["proc_time"]
        .mean()
        .reset_index()
        .rename(columns={"proc_time": "processing_time"})
    )
    result["processing_time"] = result["processing_time"].round(3)
    
    return result
```

## Postgresql

```postgresql
SELECT 
    a.machine_id,
    ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
FROM Activity a
JOIN Activity b 
    ON a.machine_id = b.machine_id 
   AND a.process_id = b.process_id
WHERE a.activity_type = 'start' 
  AND b.activity_type = 'end'
GROUP BY a.machine_id;
```
