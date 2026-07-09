# 2884. Modify Columns

## Pythondata

```pythondata
import pandas as pd

def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees["salary"] = employees["salary"] * 2
    return employees
```
