# 2883. Drop Missing Data

## Pythondata

```pythondata
import pandas as pd

def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset=["name"])
```
