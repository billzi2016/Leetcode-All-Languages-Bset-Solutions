# 2880. Select Data

## Pythondata

```pythondata
import pandas as pd

def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, ["name", "age"]]
```
