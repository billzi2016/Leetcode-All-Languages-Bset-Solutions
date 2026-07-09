# 1527. Patients With a Condition

## Mysql

```mysql
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' OR conditions LIKE '% DIAB1%';
```

## Mssql

```mssql
/* Write your T-SQL query statement below */
SELECT patient_id,
       patient_name,
       conditions
FROM   Patients
WHERE  conditions LIKE 'DIAB1%'      -- starts with DIAB1
    OR conditions LIKE '% DIAB1%';   -- contains DIAB1 after a space
```

## Oraclesql

```oraclesql
/* Write your PL/SQL query statement below */
SELECT patient_id,
       patient_name,
       conditions
FROM   Patients
WHERE  conditions LIKE 'DIAB1%' 
    OR conditions LIKE '% DIAB1%';
```

## Pythondata

```pythondata
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = (
        patients["conditions"]
        .fillna("")
        .str.split()
        .apply(lambda codes: any(code.startswith("DIAB1") for code in codes))
    )
    return patients[mask]
```

## Postgresql

```postgresql
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%' 
   OR conditions LIKE '% DIAB1%';
```
