# 2889. Reshape Data: Pivot

## Pythondata

```pythondata
import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    return weather.pivot(index='month', columns='city', values='temperature')
```
